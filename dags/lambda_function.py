from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from dotenv import find_dotenv, load_dotenv, set_key
import os
import json


# from ..time_utils import calculate_partition_date, calculate_week_dates

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

load_dotenv(dotenv_path='/opt/airflow/.env', override=True)

def calculate_week_dates(execution_date):
    """Calcula el primer y último día de la semana a partir de la fecha de ejecución."""
    # Calcular el primer día de la semana (lunes)
    # start_of_week = execution_date - timedelta(days=execution_date.weekday())
    start_of_week = execution_date

    # Calcular el último día de la semana (domingo)
    end_of_week = start_of_week + timedelta(days=6)
    
    # Formatear las fechas como cadenas si es necesario
    start_of_week_str = start_of_week.strftime('%Y-%m-%d')
    end_of_week_str = end_of_week.strftime('%Y-%m-%d')
    
    return start_of_week_str, end_of_week_str

def calculate_partition_date(execution_date):
    """Calcula el año y la semana a partir de la fecha de ejecución."""
    year = execution_date.year
    week = execution_date.isocalendar()[1]
    return year, week

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
    

def create_payload(**kwargs):
    """Crea el payload para la función Lambda"""
    
    execution_date = kwargs['execution_date']
    year, week = calculate_partition_date(execution_date=execution_date)
    start_of_week, end_of_week = calculate_week_dates(execution_date)
    
    payload = {
        "token": os.environ['API_TOKEN'],
        "start_of_week": start_of_week,
        "end_of_week": end_of_week,
        "week": week,
        'year': year
    }

    return payload
    # return json.dumps(payload).encode('utf-8')


def invoke_lambda_with_payload(**kwargs):
    task_instance = kwargs['ti']
    payload = task_instance.xcom_pull(task_ids='build_payload')
    
    # Puedes usar `json.loads` para asegurarte de que el payload sea un objeto de Python
    # payload = json.loads(payload)
    
    # Llamada al operador Lambda
    lambda_operator = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda',
        function_name='my-first-lambda',
        payload=json.dumps(payload).encode('utf-8'),  # Asegúrate de que el payload sea un JSON válido
        log_type='Tail',
        aws_conn_id='aws_default',
        region_name='eu-south-2'
    )
    
    lambda_operator.execute(kwargs)

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

    build_payload_task = PythonOperator(
    task_id='build_payload',
    python_callable=create_payload,
    provide_context=True,
    dag=dag,
)

    
    # invoke_lambda = LambdaInvokeFunctionOperator(
    #     task_id='invoke_lambda',
    #     function_name='my-first-lambda',  # Reemplaza con el nombre de tu Lambda
    #     payload='{{ task_instance.xcom_pull(task_ids="build_payload") }}',
    #     log_type='Tail',
    #     aws_conn_id='aws_default',  # Configura tu conexión a AWS en Airflow
    #     region_name='eu-south-2'
    # )

    invoke_lambda_task = PythonOperator(
        task_id='invoke_lambda_with_payload',
        python_callable=invoke_lambda_with_payload,
        provide_context=True,
        dag=dag
    )

    generate_token_task >> save_token_task >> build_payload_task >> invoke_lambda_task
