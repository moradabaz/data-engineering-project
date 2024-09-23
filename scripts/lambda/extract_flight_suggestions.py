import requests
import json
import os
import boto3
from datetime import datetime



def upload_json_to_s3(response, path='suggestions'):

    # Configurar cliente S3
    s3 = boto3.client('s3', region_name='eu-south-2')
    bucket_name = 'my-aws-project-v1'  # Reemplaza con el nombre de tu bucket

    # Nombre del archivo en S3
    data = response['data']  # Ejemplo de datos
    filename = response['filename']
    year = response['year']
    week = response['week']
    
    s3_key = f"raw/{path}/year={year}/week={week}/{filename}"

    # # Convertir datos a JSON
    json_data = json.dumps(data)

    try:
        # Subir el archivo JSON a S3
        s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_data, ContentType='application/json')
        print(f'Archivo subido exitosamente a s3://{bucket_name}/{filename}')
        return {
            'bucket': bucket_name,
            'key': s3_key,
            'path': f's3://{bucket_name}/{s3_key}'  # Ruta completa del archivo
        }
    except Exception as e:
        print(f'Error al subir el archivo: {e}')
        return {
            'error': str(e)
        }
        

def lambda_handler(event, content):

    print("Calling API....")
    
    
    #if isinstance(event, str):
    #    event = json.loads(event)  
    
    token = event.get('token')
    start_of_week = event.get('start_of_week')
    end_of_week = event.get('end_of_week')
    week = event.get('week')
    year = event.get('year')
    
    url = f'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&departureDate={start_of_week},{end_of_week}&oneWay=true&nonStop=true'

    headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
    }
    
    try:
        
        
        print(f"Fetching BASIC API.... {start_of_week}")
            # Hacer la solicitud GET a la API
        response = requests.get(url, headers=headers)
            
            # Verificar que la solicitud fue exitosa
        response.raise_for_status()
    
            # Obtener los datos de la respuesta en formato JSON
        data = response.json()
        
        response = {
            'filename': f'flighs_{start_of_week}-{end_of_week}.json',
            'year': year,
            'week': week,
            'data': data
        }
        
        # upload_json_to_s3(data)
        s3_response  = upload_json_to_s3(response)
        
        # Ingest aditional info
        
        if 'error' in s3_response:
            raise Exception(f"Error uploading to S3: {s3_response['error']}")
        
        print("[OK] Upload ....")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data processed and uploaded successfully',
                's3_status': 'UPLOADED',
                's3_path': s3_response['path'],  # Incluir la ruta completa del archivo en S3
                'data': data
            })
        }
    except requests.exceptions.HTTPError as http_err:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'error': str(http_err)})
        }
    except Exception as err:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(err)})
        }
