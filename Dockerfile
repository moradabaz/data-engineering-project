# Use the official Python image with version 3.11
FROM apache/airflow:2.8.0-python3.10

RUN python -m pip install --upgrade pip

COPY .env /opt/airflow/.env

# Ajusta los permisos si es necesario
RUN chmod 644 /opt/airflow/.env

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir "apache-airflow-providers-docker" "apache-airflow==${AIRFLOW_VERSION}" "requests==2.26.0" -r requirements.txt
