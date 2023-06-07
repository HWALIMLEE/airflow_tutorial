FROM apache/airflow:2.4.3-python3.8

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN airflow db init