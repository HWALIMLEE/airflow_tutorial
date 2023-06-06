FROM apache/airflow:2.4.2-python3.9

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

