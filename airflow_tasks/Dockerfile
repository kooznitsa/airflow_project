FROM apache/airflow:2.9.1

WORKDIR /opt/airflow

COPY ./pyproject.toml ./poetry.lock* ./

RUN pip install poetry
RUN poetry install

COPY . ./
