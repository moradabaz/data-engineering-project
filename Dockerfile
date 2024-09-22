# Use the official Python image with version 3.11
FROM apache/airflow:2.8.0-python3.10

RUN python -m pip install --upgrade pip

COPY .env /opt/airflow/.env

USER root

ENV TZ=Etc/UTC

# Establecer la zona horaria a UTC y ajustar los permisos necesarios
# RUN apt-get update && apt-get install -y tzdata \
#     && ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
#     && echo "Etc/UTC" > /etc/timezone

RUN chmod 644 /opt/airflow/.env


RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

USER airflow

# Ajusta los permisos si es necesario

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir "apache-airflow-providers-docker" "apache-airflow==${AIRFLOW_VERSION}" "requests==2.26.0" -r requirements.txt
