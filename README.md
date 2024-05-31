# Apache Airflow Project

Important notes:

- Apache Airflow is not intended for Windows. Run in Docker or in Linux environment.
- Your Python modules should be within dags/ directory.
- Do not set ```datetime.now()``` or ```date.today()``` as DAG start_date.

Notes on Airflow dependencies:

- [apache-airflow-providers-celery](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.7.0/index.html): for Celery workers.
- [sqlalchemy==1.4](https://docs.sqlalchemy.org/en/14/): Apache Airflow throws an error with SQLAlchemy > 2.0 (```sqlalchemy.exc.ArgumentError: Type annotation for "TaskInstance.dag_model" can't be correctly interpreted for Annotated Declarative Table form```). Since SQLModel works only with SQLAlchemy > 2.0, the use of both libraries is impossible. Use SQLAlchemy 1.4 instead.

## Environment variables

- POSTGRES_DB: database used by Airflow and Celery (same as in AIRFLOW__DATABASE__SQL_ALCHEMY_CONN and AIRFLOW__CELERY__RESULT_BACKEND).
- POSTGRES_API_DB: database for your API.
- AIRFLOW__CORE__FERNET_KEY: generate a fernet key:

```python
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())
```

## Docker

1. Create Docker network:

```bash
docker network create airflow-net
```

2. Build Docker containers:

```bash
docker compose up -d --build
```

3. Register a server with PGAdmin:

- Port: 5433
- User: postgres
- Host: localhost

There should be 2 databases: "airflowDB" for Airflow DAGs and Celery backend, and "apiDB" for API.

4. Apply migrations:

```bash
docker exec -it api poetry run alembic upgrade head
```

Airflow dashboard: http://localhost:8080/home

API: http://127.0.0.1:8000/docs

## Optionally: Install Airflow with Linux WSL

```bash
# 1. Create directory

cd home
mkdir airflow_project
cd airflow_project

# 2. Install pip and virtualenv

apt-get update
apt install python3-pip
pip install virtualenv
pip install virtualenv
virtualenv airflow_env
source airflow_env/bin/activate

# 3. Install Airflow

pip install apache-airflow
airflow db init

airflow users create \
          --username admin \
          --firstname admin \
          --lastname admin \
          --role Admin \
          --email email@gmail.com
          
# Password: insert password

# 4. Run the scheduler

airflow scheduler

# 5. Another terminal: run the webserver

cd airflow_project
virtualenv airflow_env
source airflow_env/bin/activate

airflow webserver
# to change the default port 8080:
# airflow webserver –port <port number>
```

Airflow dashboard will be available at http://localhost:8080/home

## Optionally: Install with a script (not tested)

```bash
# install_airflow.sh

AIRFLOW_VERSION=2.9.1

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.9.1 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

```python
# main.py

import subprocess

subprocess.call('install_airflow.sh', shell=True)
```

## Useful resources

### Airflow

- [Apache Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
- [Apache Airflow Docs: Best Practices](https://airflow.apache.org/docs/apache-airflow/2.9.1/best-practices.html)
- [Apache Airflow Docs: Cron Presets](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html#cron-presets)
- [GitHub: Apache Airflow Tutorial](https://github.com/coder2j/airflow-docker/tree/main)
- [GitHub: docker-airflow](https://github.com/marclamberti/docker-airflow/tree/main)
- [GitHub: Airflow Celery Workers (with bash scripts)](https://github.com/himewel/airflow_celery_workers/tree/main)
- [GitHub: Airflow Tutorial](https://github.com/dmlogv/airflow-tutorial/tree/master)
- [GitHub: Airflow Made Easy | Local Setup Using Docker](https://github.com/anilkulkarni87/airflow-docker/tree/main)
- [GitHub: docker-compose-CeleryExecutor.yml](https://github.com/puckel/docker-airflow/blob/master/docker-compose-CeleryExecutor.yml)
- [GitHub: Airflow Logging](https://github.com/apache/airflow/issues/38479)
- [GitHub: airflow-repo-template + Makefile](https://github.com/soggycactus/airflow-repo-template/tree/master)
- [freeCodeCamp: How to Install Apache Airflow on Windows without Docker](https://www.freecodecamp.org/news/install-apache-airflow-on-windows-without-docker/)
- [Habr: Airflow — инструмент, чтобы удобно и быстро разрабатывать и поддерживать batch-процессы обработки данных](https://habr.com/ru/companies/vk/articles/339392/)
- [Habr: Apache Airflow: делаем ETL проще](https://habr.com/ru/articles/512386/)
- [7 Common Errors to Check When Debugging Airflow DAGs](https://www.astronomer.io/blog/7-common-errors-to-check-when-debugging-airflow-dag/)

### Other

- [GitHub: Free Currency Exchange Rates API](https://github.com/fawazahmed0/exchange-api)
- [Free Weather API](https://open-meteo.com/)