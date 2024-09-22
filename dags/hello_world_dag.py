from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

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

def calculate_week_dates(execution_date):
    """Calcula el primer y último día de la semana a partir de la fecha de ejecución."""
    # Calcular el primer día de la semana (lunes)
    start_of_week = execution_date - timedelta(days=execution_date.weekday())
    
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


def create_payload(**kwargs):
    """Crea el payload para la función Lambda"""
    
    execution_date = kwargs['execution_date']
    year, week = calculate_partition_date(execution_date=execution_date)
    start_of_week, end_of_week = calculate_week_dates(execution_date)
    
    payload = {
        "start_of_week": start_of_week,
        "end_of_week": end_of_week,
        "week": week,
        'year': year
    }

    print(f"Payload: {payload}")  # Imprime el payload para verificar su estructura
    
    return payload

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='Un DAG simple que imprime Hola Mundo',
    schedule_interval='@daily',
    catchup=False
)

build_payload_task = PythonOperator(
    task_id='build_payload',
    python_callable=create_payload,
    provide_context=True,
    dag=dag,
)