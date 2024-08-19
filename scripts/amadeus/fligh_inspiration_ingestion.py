import requests
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
print(os.path.abspath(os.path.dirname(__file__)))

# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
# from .aws_tools import upload_json_to_s3
from scripts.amadeus.aws_tools import upload_json_to_s3



load_dotenv()

def fetch_data_from_api():
    # Endpoint de la API a la que quieres hacer la solicitud
    url = os.getenv('AMADEUS_FLIGHT_INSPIRATION_URL')
    # token = os.getenv('AMADEUS_TOKEN')
    token = 'mkVObwQmKfcno7LGx600EiSwA4Cs'
    print(f'token {token}')

    # Cabeceras para la solicitud
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    try:
        # Hacer la solicitud GET a la API
        response = requests.get(url, headers=headers)
        
        # Verificar que la solicitud fue exitosa
        response.raise_for_status()

        # Obtener los datos de la respuesta en formato JSON
        data = response.json()
        
        upload_json_to_s3(data)

        # Definir el nombre del archivo JSON donde se guardará la respuesta
        # json_file = 'response_data_aLT.json'

        # # Guardar los datos en el archivo JSON
        # with open(json_file, 'w') as file:
        #     json.dump(data, file, indent=4)

        print(f'Datos guardados exitosamente en AWS')

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except Exception as err:
        print(f'Error: {err}')

# Llamar a la función para obtener los datos y guardarlos en un archivo JSON
fetch_data_from_api()
