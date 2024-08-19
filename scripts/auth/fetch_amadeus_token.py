import requests
from dotenv import find_dotenv, load_dotenv, set_key
import os

env_path = find_dotenv()
if env_path:
    print(f'Archivo .env encontrado: {env_path}')
else:
    print('Archivo .env no encontrado.')

# Cargar variables existentes en el archivo .env
load_dotenv(find_dotenv())


def fetch_token():
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'  # URL de la API para obtener el token
    
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
        
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

        return access_token

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except Exception as err:
        print(f'Error: {err}')

# Ejecutar la función para obtener y guardar el token
fetch_token()
