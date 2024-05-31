import asyncio
from datetime import timedelta
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

from common.parsers.currency import CurrencyParser


def get_currencies():
    asyncio.run(CurrencyParser().get_currencies())


with DAG(
    dag_id='currency_dag',
    start_date=pendulum.datetime(2024, 5, 29, tz='UTC'),
    schedule=timedelta(minutes=5),
    catchup=False,
) as dag:
    currencies_task = PythonOperator(
        task_id='get_currency_task',
        python_callable=get_currencies,
    )

    currencies_task
