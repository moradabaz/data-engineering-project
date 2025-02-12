from datetime import timedelta
import json
import time
from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from airflow.providers.amazon.aws.operators.athena import AthenaOperator
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.dummy import DummyOperator
from airflow.exceptions import AirflowFailException
import boto3
import pandas as pd
import pyarrow.parquet as pq
import io
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task, task_group
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path='/opt/airflow/.env', override=True)


S3_BUCKET = "my-aws-project-v1"

# Directorios de datos
S3_PREFIX_AMADEUS = "raw/suggestions_info/amadeus/"
S3_PREFIX_SKYSCANNER = "raw/suggestions_info/skyscanner/"

# Glue Jobs
GLUE_JOB_AMADEUS = "amadeus_flights_info"
GLUE_JOB_SKYSCANNER = "skyscanner_flights_info"

# Glue Crawlers (Opcional)
GLUE_CRAWLER_AMADEUS = "amadeus_flights_crawler"
GLUE_CRAWLER_SKYSCANNER = "skyscanner_flights_crawler"

AWS_CONN_ID = "aws_default"
ATHENA_DATABASE = "flights-db"
ATHENA_OUTPUT_S3 = "s3://my-aws-project-v1/queries/amadeus/on_demand/"
LAMBDA_FUNCTION_NAME = "get-flights-delay-prediction"


bucket_name = os.environ['S3_BUCKET_NAME']
amadeus_filepath = os.environ['AMADEUS_FILES_PATH']
amadeus_raw_crawler = os.environ['AMADEUS_GLUE_RAW_CRAWLER']
amadeus_trans_crawler = os.environ['AMADEUS_GLUE_TRANS_CRAWLER'] 
skyscanner_filepath = os.environ['SKYSCANNER_FILES_PATH']
skyscanner_raw_crawler = os.environ['SKYSCANNER_GLUE_RAW_CRAWLER']
skyscanner_trans_crawler = os.environ['SKYSCANNER_GLUE_TRANS_CRAWLER']


# Configuración por defecto del DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': days_ago(1)
}

# Definir el DAG
with DAG(
    dag_id='transform_raw_data_dag',
    default_args=default_args,
    description='This DAG detects new files to execute a glue job to transform the data',
    schedule_interval=None,  # Se ejecuta cuando detecta nuevos archivos
    max_active_runs=1
) as dag:
    
    start = DummyOperator(task_id="start")
    
    @task_group(group_id='extract_flights_delay_prediction')
    def extract_flights_delay_prediction():
        
        # Run First Lambda

        get_athena_flights_query = LambdaInvokeFunctionOperator(
            task_id="get_athena_flights_query",
            function_name="GetAmadeusOnDemandFlight",
            log_type="Tail",
            aws_conn_id=AWS_CONN_ID,
            region_name='eu-south-2',
            do_xcom_push=True,
            dag=dag
        )

        # 🔹 1️⃣ Ejecutar la consulta en Athena y obtener QueryExecutionId
        def extract_results(**kwargs):
            ti = kwargs['ti']
            response = ti.xcom_pull(task_ids='extract_flights_delay_prediction.get_athena_flights_query')
            if not response:
                raise AirflowFailException("❌ No response received from Lambda.")
            response = json.loads(response)
            if response is None or response["statusCode"] != 200:
                raise AirflowFailException(f"Lambda has failed")
            results = json.loads(response["body"])["ResultSet"]
            payload = {
                "token": os.environ["API_TOKEN"],
                "results": results
            }
            print(payload)
            return json.dumps(payload)

        extract_results_task = PythonOperator(
            task_id="extract_results_task",
            python_callable=extract_results,
            provide_context=True,
            dag=dag
        )

        process_results_lambda = LambdaInvokeFunctionOperator(
            task_id="process_results_lambda",
            function_name="ProcessDelayedPredictionFlights",
            payload="{{ task_instance.xcom_pull(task_ids='extract_flights_delay_prediction.extract_results_task') }}",
            log_type="Tail",
            aws_conn_id=AWS_CONN_ID,
            region_name='eu-south-2',
            dag=dag
        )

        delay_prediction_raw_crawler = GlueCrawlerOperator(
            task_id="delay_prediction_raw_crawler",
            aws_conn_id="aws_default",
            config={"Name": 'delay-raw'},
            region_name="eu-south-2",  # Cambia a tu región
            dag=dag,
        )

        delay_prediction_glue_job = GlueJobOperator(
            task_id="delay_prediction_glue_job",
            job_name='delayed_flights_prediction',
            iam_role_name='AWSGlueServiceRole-amadeus',
            create_job_kwargs={'GlueVersion': '4.0'},
            aws_conn_id="aws_default",
            region_name="eu-south-2",
            execution_timeout=timedelta(minutes=60),
            dag=dag
        )

        delay_prediction_transformed_crawler = GlueCrawlerOperator(
            task_id="delay_prediction_transformed_crawler",
            config={"Name": 'delay-transformed'},
            aws_conn_id="aws_default",
            region_name="eu-south-2",  # Cambia a tu región
            dag=dag,
        )

        get_athena_flights_query >> extract_results_task >> process_results_lambda >> delay_prediction_raw_crawler >> delay_prediction_glue_job >> delay_prediction_transformed_crawler
        
           
    @task_group(group_id = 'amadeus_data_extraction')
    def amadeus_data_extraction():
        
        # detect_new_amadeus_json = S3KeySensor(
        #     task_id="detect_new_amadeus_json",
        #     bucket_name=S3_BUCKET,
        #     bucket_key=f"{S3_PREFIX_AMADEUS}*.json",
        #     wildcard_match=True,
        #     aws_conn_id="aws_default",
        #     timeout=600,
        #     poke_interval=60,
        #     dag=dag
        # )

        amadeus_glue_raw_crawler = GlueCrawlerOperator(
            task_id="amadeus_glue_raw_crawler",
            aws_conn_id="aws_default",
            config={"Name": amadeus_raw_crawler},
            region_name="eu-south-2",  # Cambia a tu región
            dag=dag,
        )

        amadeus_glue_job = GlueJobOperator(
            task_id="amadeus_glue_job",
            job_name=GLUE_JOB_AMADEUS,
            iam_role_name='AWSGlueServiceRole-amadeus',
            create_job_kwargs={'GlueVersion': '4.0'},
            aws_conn_id="aws_default",
            region_name="eu-south-2",
            execution_timeout=timedelta(minutes=60),
            dag=dag
        )

        amadeus_glue_transformed_crawler = GlueCrawlerOperator(
            task_id="run_glue_transformed_crawler",
            config={"Name": amadeus_trans_crawler},
            aws_conn_id="aws_default",
            region_name="eu-south-2",  # Cambia a tu región
            dag=dag,
        )

        amadeus_glue_raw_crawler >> amadeus_glue_job >> amadeus_glue_transformed_crawler
    
    @task_group(group_id = 'skyscanner_data_extraction')
    def skyscanner_data_extraction():
        
        # detect_new_skyscanner_json = S3KeySensor(
        #     task_id="detect_new_skyscanner_json",
        #     bucket_name=S3_BUCKET,
        #     bucket_key=f"{S3_PREFIX_SKYSCANNER}*.json",
        #     wildcard_match=True,
        #     aws_conn_id="aws_default",
        #     timeout=600,
        #     poke_interval=60,
        #     dag=dag
        # )

        skyscanner_glue_raw_crawler = GlueCrawlerOperator(
            task_id="skyscanner_glue_raw_crawler",
            config={"Name": skyscanner_raw_crawler},
            aws_conn_id="aws_default",
            region_name="eu-south-2",  # Cambia a tu región
            dag=dag,
        )

        skyscanner_glue_job = GlueJobOperator(
            task_id="skyscanner_glue_job",
            job_name=GLUE_JOB_SKYSCANNER,
            iam_role_name='AWSGlueServiceRole-amadeus',
            create_job_kwargs={'GlueVersion': '3.0'},
            aws_conn_id="aws_default",
            region_name="eu-south-2",
            execution_timeout=timedelta(minutes=60),
            dag=dag
        )

        skyscanner_glue_transformed_crawler = GlueCrawlerOperator(
            task_id="skyscanner_glue_transformed_crawler",
            config={"Name": skyscanner_trans_crawler},
            aws_conn_id="aws_default",
            region_name="eu-south-2",  # Cambia a tu región
            dag=dag,
        )

        skyscanner_glue_raw_crawler >> skyscanner_glue_job >> skyscanner_glue_transformed_crawler

    start >> [amadeus_data_extraction(), skyscanner_data_extraction()] >> extract_flights_delay_prediction()

    