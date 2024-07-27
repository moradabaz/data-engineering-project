# Use the official Python image with version 3.11
FROM apache/airflow:2.8.0-python3.10

RUN python -m pip install --upgrade pip

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" "requests==2.26.0" -r requirements.txt
