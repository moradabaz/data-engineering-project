import requests
import json


url = 'https://sky-scanner3.p.rapidapi.com/flights/search-one-way?fromEntityId=MAD&toEntityId=LIS&departDate=2024-08-28&stops=direct'

headers = {
    'x-rapidapi-host': "sky-scanner3.p.rapidapi.com",
    'x-rapidapi-key': "8a084f1aebmsh4e2a4756ff071d4p12ff6bjsn62affbba6a02"
}
response = requests.get(url, headers=headers)
        
        # Verificar que la solicitud fue exitosa
response.raise_for_status()

        # Obtener los datos de la respuesta en formato JSON
data = response.json()

        # Definir el nombre del archivo JSON donde se guardará la respuesta
json_file = 'response_data_aLT.json'

        # # Guardar los datos en el archivo JSON
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)