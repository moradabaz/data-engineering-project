import boto3
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def upload_json_to_s3(data):
    # Configurar cliente S3
    s3 = boto3.client('s3', region_name='eu-south-2')
    bucket_name = os.getenv("S3_BUCKET_NAME")  # Reemplaza con el nombre de tu bucket

    # Nombre del archivo en S3
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'flight_suggestions_{timestamp}.json'

    # # Convertir datos a JSON
    json_data = json.dumps(data)

    try:
        # Subir el archivo JSON a S3
        s3.put_object(Bucket=bucket_name, Key=filename, Body=json_data, ContentType='application/json')
        print(f'Archivo subido exitosamente a s3://{bucket_name}/{filename}')
    except Exception as e:
        print(f'Error al subir el archivo: {e}')
