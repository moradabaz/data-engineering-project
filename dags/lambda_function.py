from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from dotenv import find_dotenv, load_dotenv, set_key
import os
import requests
import json

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

load_dotenv(dotenv_path='/opt/airflow/.env', override=True)

def save_token_f(token):
    Variable.delete('API_TOKEN')
    Variable.set("API_TOKEN", token)
    print(f"Token guardado: {token}")

def save_token_to_env(**kwargs):
    task_instance = kwargs['ti']
    response  = task_instance.xcom_pull(task_ids='generate_token_task')
    response = json.loads(response)
    token = response['token'].strip('"')
    print(f'token received: {token}')
    
    try:
        set_key(dotenv_path=find_dotenv(), key_to_set='API_TOKEN', value_to_set=token)
    except Exception as e:
        print(f'Error al guardar el token en el entorno: {e}')
        return 'success'
    


with DAG(dag_id='lambda_example_dag', default_args=default_args, schedule_interval=None, max_active_runs=1) as dag:
    
    payload = {"client_id": os.getenv('CLIENT_ID'), "client_secret": os.getenv('CLIENT_SECRET')}
    playload_bytes = json.dumps(payload).encode('utf-8')
    
    generate_token_task = LambdaInvokeFunctionOperator(
        task_id='generate_token_task',
        function_name='generate-token-function',
        log_type='Tail',
        payload=playload_bytes,
        aws_conn_id='aws_default',  # Configura tu conexión a AWS en Airflow
        region_name='eu-south-2'
    )

    save_token_task = PythonOperator(
        task_id='save_token_task',
        python_callable=save_token_to_env,
        provide_context=True,
        dag=dag
    )
    
    invoke_lambda = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda',
        function_name='my-first-lambda',  # Reemplaza con el nombre de tu Lambda
        payload=json.dumps({ 'token': os.environ['API_TOKEN']}).encode('utf-8'),
        log_type='Tail',
        aws_conn_id='aws_default',  # Configura tu conexión a AWS en Airflow
        region_name='eu-south-2'
    )

    generate_token_task >> save_token_task >> invoke_lambda
