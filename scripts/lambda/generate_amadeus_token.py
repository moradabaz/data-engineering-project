import json
import requests

def lambda_handler(event, context):
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'  # URL de la API para obtener el token
    
    client_id = event['client_id']
    client_secret = event['client_secret']
    
    print(f'client id -> {client_id}')
        
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        # Hacer la solicitud POST para obtener el token
        response = requests.post(url, headers=headers, data=data)
        
        # Verificar que la solicitud fue exitosa
        response.raise_for_status()

        # Obtener los datos de la respuesta en formato JSON
        token_data = response.json()
        access_token = token_data.get('access_token')
        
        #env_path = find_dotenv()
        #set_key(env_path, 'API_TOKEN', access_token)
        #print(f'Token guardado en {env_path}')

        return {
            'statusCode': 200,
            'token': json.dumps(access_token)
        }

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
        return {
            'statusCode': 500
        }
    except Exception as err:
        print(f'Error: {err}')
   
