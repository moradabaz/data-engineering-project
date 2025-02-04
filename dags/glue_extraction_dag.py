from datetime import timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task, task_group
from dotenv import find_dotenv, load_dotenv, set_key
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
    catchup=False,
    max_active_runs=1
) as dag:
    
    start = DummyOperator(task_id="start")
    
    @task_group(group_id='extract_flights_delay_prediction')
    def extract_flights_delay_prediction():
        pass
           
    # @task_group(group_id = 'amadeus_data_extraction')
    # def amadeus_data_extraction():
        
    #     detect_new_amadeus_json = S3KeySensor(
    #         task_id="detect_new_amadeus_json",
    #         bucket_name=S3_BUCKET,
    #         bucket_key=f"{S3_PREFIX_AMADEUS}*.json",
    #         wildcard_match=True,
    #         aws_conn_id="aws_default",
    #         timeout=600,
    #         poke_interval=60,
    #         dag=dag
    #     )

    #     amadeus_glue_raw_crawler = GlueCrawlerOperator(
    #         task_id="amadeus_glue_raw_crawler",
    #         aws_conn_id="aws_default",
    #         config={"Name": amadeus_raw_crawler},
    #         region_name="eu-south-2",  # Cambia a tu región
    #         dag=dag,
    #     )

    #     amadeus_glue_job = GlueJobOperator(
    #         task_id="amadeus_glue_job",
    #         job_name=GLUE_JOB_AMADEUS,
    #         iam_role_name='AWSGlueServiceRole-amadeus',
    #         create_job_kwargs={'GlueVersion': '4.0'},
    #         aws_conn_id="aws_default",
    #         region_name="eu-south-2",
    #         execution_timeout=timedelta(minutes=60),
    #         dag=dag
    #     )

    #     amadeus_glue_transformed_crawler = GlueCrawlerOperator(
    #         task_id="run_glue_transformed_crawler",
    #         config={"Name": amadeus_trans_crawler},
    #         aws_conn_id="aws_default",
    #         region_name="eu-south-2",  # Cambia a tu región
    #         dag=dag,
    #     )

    #     amadeus_glue_raw_crawler >> amadeus_glue_job >> amadeus_glue_transformed_crawler
    
    # @task_group(group_id = 'skyscanner_data_extraction')
    # def skyscanner_data_extraction():
        
    #     detect_new_skyscanner_json = S3KeySensor(
    #         task_id="detect_new_skyscanner_json",
    #         bucket_name=S3_BUCKET,
    #         bucket_key=f"{S3_PREFIX_SKYSCANNER}*.json",
    #         wildcard_match=True,
    #         aws_conn_id="aws_default",
    #         timeout=600,
    #         poke_interval=60,
    #         dag=dag
    #     )

    #     skyscanner_glue_raw_crawler = GlueCrawlerOperator(
    #         task_id="skyscanner_glue_raw_crawler",
    #         config={"Name": skyscanner_raw_crawler},
    #         aws_conn_id="aws_default",
    #         region_name="eu-south-2",  # Cambia a tu región
    #         dag=dag,
    #     )

    #     skyscanner_glue_job = GlueJobOperator(
    #         task_id="skyscanner_glue_job",
    #         job_name=GLUE_JOB_SKYSCANNER,
    #         iam_role_name='AWSGlueServiceRole-amadeus',
    #         create_job_kwargs={'GlueVersion': '3.0'},
    #         aws_conn_id="aws_default",
    #         region_name="eu-south-2",
    #         execution_timeout=timedelta(minutes=60),
    #         dag=dag
    #     )

    #     skyscanner_glue_transformed_crawler = GlueCrawlerOperator(
    #         task_id="skyscanner_glue_transformed_crawler",
    #         config={"Name": skyscanner_trans_crawler},
    #         aws_conn_id="aws_default",
    #         region_name="eu-south-2",  # Cambia a tu región
    #         dag=dag,
    #     )

    #     skyscanner_glue_raw_crawler >> skyscanner_glue_job >> skyscanner_glue_transformed_crawler

    # start >> [amadeus_data_extraction(), skyscanner_data_extraction()]