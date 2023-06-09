import os
from datetime import timedelta, datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator

from src.movie_data import download_data_to_bigquery, get_count_over_4, delete_movie_data, \
    load_data_from_bigquery, is_exists

seoul_time = pendulum.timezone('Asia/Seoul')
dag_name = os.path.basename(__file__).split('.')[0]

default_args = {
    'owner': 'hwalim',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id=dag_name,
    default_args=default_args,
    description='',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1, 17, 30, tzinfo=seoul_time),
    catchup=False,
    tags=['etl']
) as dag:
    check_data = BranchPythonOperator(
        task_id='is_exists',
        python_callable=is_exists
    )
    download_data = PythonOperator(
        task_id='download_data_to_bigquery',
        python_callable=download_data_to_bigquery
    )
    get_data = PythonOperator(
        task_id='get_movie_data',
        python_callable=load_data_from_bigquery
    )
    get_count = PythonOperator(
        task_id='get_count_over_4',
        python_callable=get_count_over_4,
        trigger_rule='one_success'
    )
    delete_data = PythonOperator(
        task_id='delete_data_from_bigquery',
        python_callable=delete_movie_data
    )
    check_data >> [download_data, get_data] >> get_count >> delete_data

