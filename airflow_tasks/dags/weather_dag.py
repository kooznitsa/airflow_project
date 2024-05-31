import asyncio
from datetime import timedelta
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

from common.parsers.weather import WeatherParser


def get_weather():
    asyncio.run(WeatherParser().get_weather())


with DAG(
    dag_id='weather_dag',
    start_date=pendulum.datetime(2024, 5, 29, tz='UTC'),
    schedule=timedelta(minutes=2),
    catchup=False,
) as dag:
    weather_task = PythonOperator(
        task_id='get_weather_task',
        python_callable=get_weather,
    )

    weather_task
