from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.operators.python import PythonOperator
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

load_dotenv()


def generate_token(**kwargs):
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'  # URL de la API para obtener el token
    
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    
    print(f'client id -> {client_id}')
        
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        # Hacer la solicitud POST para obtener el token
        response = requests.post(url, headers=headers, data=data)
        
        # Verificar que la solicitud fue exitosa
        response.raise_for_status()

        # Obtener los datos de la respuesta en formato JSON
        token_data = response.json()
        access_token = token_data.get('access_token')
        
        env_path = find_dotenv()
        set_key(env_path, 'API_TOKEN', access_token)
        print(f'Token guardado en {env_path}')

        return access_token

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except Exception as err:
        print(f'Error: {err}')

with DAG(dag_id='lambda_example_dag', default_args=default_args, schedule_interval=None, max_active_runs=1) as dag:
    
    generate_token_task = PythonOperator(
        task_id='generate_token',
        python_callable=generate_token,
        provide_context=True,
    )
    
    payload = { 'token': os.getenv('API_TOKEN') }
    payload_bytes = json.dumps(payload).encode('utf-8')


    invoke_lambda = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda',
        function_name='my-first-lambda',  # Reemplaza con el nombre de tu Lambda
        payload=payload_bytes,
        log_type='Tail',
        aws_conn_id='aws_default',  # Configura tu conexión a AWS en Airflow
        region_name='eu-south-2'
    )

    generate_token_task >> invoke_lambda
