from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from datetime import datetime, timedelta

# TODO: Define 
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

# Configuración por defecto del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Definir el DAG
with DAG(
    dag_id='transforafsdfm_raw_data_dag',
    default_args=default_args,
    description='This DAG detects new files to execute a glue job to transform the data',
    schedule_interval=None,  # Se ejecuta cuando detecta nuevos archivos
    catchup=False,
    max_active_runs=1
) as dag:

    detect_new_skyscanner_json = S3KeySensor(
        task_id="detect_new_skyscanner_json",
        bucket_name=S3_BUCKET,
        bucket_key=f"{S3_PREFIX_SKYSCANNER}*.json",
        wildcard_match=True,
        aws_conn_id="aws_default",
        timeout=600,
        poke_interval=60,
        dag=dag
    )

    run_glue_job_skyscanner = GlueJobOperator(
        task_id="run_glue_job_skyscanner",
        job_name=GLUE_JOB_SKYSCANNER,
        iam_role_name='AWSGlueServiceRole-amadeus',
        create_job_kwargs={'GlueVersion': '4.0'},
        aws_conn_id="aws_default",
        region_name="eu-south-2",
        execution_timeout=timedelta(minutes=60),
        dag=dag
    )

    #detect_new_skyscanner_json
    run_glue_job_skyscanner