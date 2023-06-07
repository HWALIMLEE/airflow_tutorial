#!/bin/bash
dag_id="$1"
owner="$2";
retries="$3";
retry_delay="$4";
description="$5";
schedule_interval="$6";
start_date="$7";
catchup="$8";
tags="$9";
dir="$(pwd)/dags"

cat > ${dir}/${dag_id}.py << EOF
import os
from datetime import timedelta, datetime
import pendulum
from airflow import DAG

seoul_time = pendulum.timezone('Asia/Seoul')
dag_name = os.path.basename(__file__).split('.')[0]

default_args = {
    'owner': '${owner}',
    'retries': ${retries},
    'retry_delay': timedelta(minutes=${retry_delay})
}

with DAG(
    dag_id=dag_name,
    default_args=default_args,
    description='${description}',
    schedule_interval='${schedule_interval}',
    start_date=datetime(${start_date}, tzinfo=seoul_time),
    catchup=${catchup},
    tags=${tags}
) as dag:
EOF