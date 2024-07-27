from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("Hola Mundo")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='Un DAG simple que imprime Hola Mundo',
    schedule_interval='@daily'
)

hello_world_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)
