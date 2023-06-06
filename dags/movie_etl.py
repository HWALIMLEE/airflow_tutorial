import os
from datetime import timedelta, datetime
import pendulum
from airflow import DAG

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
    pass
