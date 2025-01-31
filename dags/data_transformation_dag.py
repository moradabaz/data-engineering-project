from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from airflow.utils.dates import days_ago
from dotenv import find_dotenv, load_dotenv, set_key
import os


load_dotenv(dotenv_path='/opt/airflow/.env', override=True)

bucket_name = os.environ['S3_BUCKET_NAME']
amadeus_filepath = os.environ['AMADEUS_FILES_PATH']
amadeus_crawler_name = os.environ['AMADEUS_GLUE_CRAWLER']


# Configuración por defecto del DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': days_ago(1)
}

dag = DAG(
    'data_transformation_dag',
    default_args=default_args,
    description='DAG que escanea nuevos datos en S3 y ejecuta un Glue Job para procesar información de vuelos',
    schedule_interval='@daily',
    catchup=False
)

# check_new_files_task = S3KeySensor(
#     task_id='check_new_files_task',
#     bucket_name=bucket_name,  # Reemplaza con tu bucket S3
#     bucket_key=amadeus_filepath,
#     aws_conn_id='aws_default',
#     wildcard_match=True,
#     poke_interval=60 * 10,
#     timeout=60 * 60 * 24,
#     dag=dag
# )

run_amadeus_glue_job_task = GlueJobOperator(
    task_id='run_amadeus_glue_job_task',
    job_name='amadeus_flights_info',
    script_location='s3://my-aws-project-v1/scripts/glue/amadeus_flights_info.py',
    aws_conn_id='aws_default',
    iam_role_name='AWSGlueServiceRole-amadeus',
    region_name=os.environ['S3_REGION'],  # Especifica tu región de AWS
    create_job_kwargs={'GlueVersion': '3.0'},
    dag=dag
)

# run_glue_crawler = GlueCrawlerOperator(
#     task_id='run_glue_crawler',
#     config={"Name": amadeus_crawler_name},  # Reemplaza con el nombre del Glue Crawler
#     aws_conn_id='aws_default',
#     dag=dag
# )

run_amadeus_glue_job_task