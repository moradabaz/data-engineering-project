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
    
    s3_key = f"raw/{path}/{filename}"

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

def download_amadeus_info(data_info):
    print("Download amadeus additional info...")
    url = data_info['url']
    token = data_info['token']
    start_of_week = data_info['start_of_week']
    end_of_week = data_info['end_of_week']
    year = data_info['year']
    week = data_info['week']
    origin = data_info['origin']
    destination = data_info['destination']
    departureDate = data_info['departureDate']
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    try:
        
        
        print('fetching response...')
        # Hacer la solicitud GET a la API
        response = requests.get(url, headers=headers)
            
            # Verificar que la solicitud fue exitosa
        response.raise_for_status()
    
        # Obtener los datos de la respuesta en formato JSON
        data = response.json()
        
        splitted_date = departureDate.split('-')
        
        year = splitted_date[0]
        month = splitted_date[1]
        day = splitted_date[2]
                
        filename = f'ori={origin}/dest={destination}/year={year}/month={month}/week={week}/day={day}/flights_info_{origin}_{destination}_{departureDate}.json'
        
        data_info['filename'] = filename
        
        data_info['data'] = data
        
        print(response)
        
        # upload_json_to_s3(data)
        print("Storing amadeus additional infor....")
        s3_response = upload_json_to_s3(data_info, path='suggestions_info/amadeus')
        
        if 'error' in s3_response:
            raise Exception(f"Error uploading to S3: {s3_response['error']}")
        
        print("[OK] Upload ....")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Amadeus additional info uploaded successfully',
                's3_status': 'UPLOADED',
                's3_path': s3_response['path'],  # Incluir la ruta completa del archivo en S3
            })
        }
        

    except requests.exceptions.HTTPError as http_err:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'error': str(http_err)})
        }

def download_skyscanner_info(data_info):
    
    origin = data_info['origin']
    destination = data_info['destination']
    start_of_week = data_info['start_of_week']
    end_of_week = data_info['end_of_week']
    year = data_info['year']
    week = data_info['week']
    departureDate = data_info['departureDate']
    
    try: 
        url = f'https://sky-scanner3.p.rapidapi.com/flights/search-one-way?fromEntityId={origin}&toEntityId={destination}&departDate={departureDate}&stops=direct'
        
        headers = {
            'x-rapidapi-host': "sky-scanner3.p.rapidapi.com",
            'x-rapidapi-key': "8a084f1aebmsh4e2a4756ff071d4p12ff6bjsn62affbba6a02"
        }
        response = requests.get(url, headers=headers)
                
                # Verificar que la solicitud fue exitosa
        response.raise_for_status()
        
        # Obtener los datos de la respuesta en formato JSON
        data = response.json()

        data_info['data'] = data
        
        splitted_date = departureDate.split('-')
        
        year = splitted_date[0]
        month = splitted_date[1]
        day = splitted_date[2]
                
        filename = f'ori={origin}/dest={destination}/year={year}/month={month}/week={week}/day={day}/flights_info_{origin}_{destination}_{departureDate}.json'
        
        # filename = f'flights_info_{origin}_{destination}_{departureDate}.json'
        
        data_info['filename'] = filename
        
        s3_response = upload_json_to_s3(data_info, path='suggestions_info/skyscanner')
        
        if 'error' in s3_response:
            raise Exception(f"Error uploading to S3: {s3_response['error']}")
        
        print("[OK] Upload ....")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Skycanner additional info uploaded successfully',
                's3_status': 'UPLOADED',
                's3_path': s3_response['path'],  # Incluir la ruta completa del archivo en S3
            })
        }
    
    except requests.exceptions.HTTPError as http_err:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'error': str(http_err)})
    }

def lambda_handler(event, context):
    # TODO implement
    
    fights_data = event['data']
    token = event['token']
    
    for flight in fights_data:
        url = flight['links']['flightOffers']
        origin = flight['origin']
        destination = flight['destination']
        data_info = {
            'url': url,
            'token': token,
            'start_of_week': event['start_of_week'],
            'end_of_week': event['end_of_week'],
            'year': event['year'],
            'week': event['week'],
            'origin': flight['origin'],
            'destination': flight['destination'],
            'departureDate': flight['departureDate']
        }
        try:
            print(f'Fetching Amadeus data for {origin} -> {destination}')
            download_amadeus_info(data_info)
            
            print(f'Fetching Skycanner data for {origin} -> {destination}')
            download_skyscanner_info(data_info)
            
        except Exception as err:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(err)})
            }
    return {
        'statusCode': 200,
        'body':  "everything OK"
    }