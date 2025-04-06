from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
import processing


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 5),
}

dag = DAG(
    dag_id='user_recordings_2017',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

etl_task = PythonOperator(
    task_id='run_user_recordings_2017',
    python_callable=user_recordings_2017,
    dag=dag,
)
