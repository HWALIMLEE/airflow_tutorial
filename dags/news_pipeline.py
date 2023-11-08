import os
from datetime import timedelta, datetime
import pendulum

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

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
    description='news dashboard 운영을 위해 1시간마다 돌아가는 dag 입니다.',
    schedule_interval='0 * * * *',
    start_date=datetime(2023, 1, 1, tzinfo=seoul_time),
    catchup=False,
    tags=['pseudo']
) as dag:
    get_news = KubernetesPodOperator(
        task_id='news_to_es',
        image="asia-northeast3-docker.pkg.dev/serious-unison-403913/app-images/news",
        image_pull_policy='Always'
    )
    get_news
