FROM apache/airflow:2.4.3-python3.8

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# BigQuery credentials add
ENV GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/dags/supports/bigquery_credentials.json

RUN airflow db init