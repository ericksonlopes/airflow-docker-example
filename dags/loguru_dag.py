from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from project.create_file import create_file

default_args = {
    'owner': 'erickson',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('dag_loguru', default_args=default_args, schedule=timedelta(minutes=2), catchup=False,
         tags=['loguru', 'test']) as dag:
    doc_md = __doc__

    dag_loguru = PythonOperator(
        task_id='dag_loguru_id',
        python_callable=create_file
    )
