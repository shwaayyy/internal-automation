from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'wahyu',
    'start_date': datetime(2023, 5, 22),
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='dag_selenium_task',
    default_args=default_args,
    description='a simple DAG from YAHAHAHA WAHYU',
    schedule_interval='0 0 * * *'
)


def task1():
    print('hello world')


def task2():
    print('hello universe')


t1 = PythonOperator(
    task_id='task1',
    python_callable=task1,
    dag=dag,
)

t2 = PythonOperator(
    task_id='task2',
    python_callable=task2,
    dag=dag,
)

t1 >> t2
