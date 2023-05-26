from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def say_hello():
    print("Hello, Airflow!")

# Define the DAG
dag = DAG(
    'hello_world',
    description='A simple DAG that prints "Hello, Airflow!"',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
)

# Define the task
task = PythonOperator(
    task_id='print_hello',
    python_callable=say_hello,
    dag=dag,
)

# Set task dependencies
task

