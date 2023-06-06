AIRFLOW_CONFIG := AIRFLOW_HOME=/opt/airflow AIRFLOW_UID=50000 AIRFLOW_GID=0
init:
	docker build . -t airflow:2.4.2

start: # Docker compose 를 통해 Airflow 실행
	$(AIRFLOW_CONFIG) docker-compose -f docker-compose.yml up -d

stop: # Docker compose 를 통해 실행한 Airflow 종료
	$(AIRFLOW_CONFIG) docker-compose down


.PHONY: create
create:
	@python dag_code_generator.py
