import os
from datetime import timedelta, datetime
import pendulum
from airflow import DAG
from airflow.decorators import task

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './config/bigquery_credentials.json'

from movie_data import download_data_to_bigquery

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
    # download_data = PythonOperator(
    #     task_id='download_data_to_bigquery',
    #     python_callable=download_data_to_bigquery
    # )

    # get_average = PythonOperator(
    #     task_id='get_rating_average',
    #     python_callable=get_rating_average
    # )
    #
    # mail = PythonOperator(
    #     task_id='send_mail',
    #     python_callable=send_mail
    # )
    @task
    def test():
        print('test')
    test()
