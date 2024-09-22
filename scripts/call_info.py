
def download_amadeus_info(data_info):
    print("Download amadeus additional info...")
    url = data_info['url']
    token = data_info['token']
    start_of_week = data_info['start_of_week']
    end_of_week = data_info['end_of_week']
    year = data_info['year']
    week = data_info['week']
    
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
        
        print('so far, so good')
        
        response = {
            'filename': f'flights_info_{start_of_week}-{end_of_week}.json',
            'year': year,
            'week': week,
            'data': data
        }
        
        # upload_json_to_s3(data)
        print("Fetching amadeus additional infor....")
        json_data = upload_json_to_s3(response, path='suggestion_info/amadeus')

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
        
        response = {
            'filename': f'flights_info_{start_of_week}-{end_of_week}.json',
            'year': year,
            'week': week,
            'data': data
        }
        
        json_data = upload_json_to_s3(response, path='suggestion_info/skyscanner')
        
        return {
            'statusCode': 200,
            'body': json_data
        }
    except requests.exceptions.HTTPError as http_err:
        return None

    
def download_flights_info(data_info):

    for flight in data:
        url = flight['links']['flightOffers']
        origin = flight['origin']
        destination = flight['destination']
        data_info = {
            'url': url,
            'token': data_info['token'],
            'start_of_week': data_info['start_of_week'],
            'end_of_week': data_info['end_of_week'],
            'year': data_info['year'],
            'week': data_info['week'],
            'origin': flight['origin'],
            'destination': flight['destination'],
            'departureDate': flight['departureDate']
        }
        download_amadeus_info(data_info)
        #download_skyscanner_info(data_info)
        
    return {
            'statusCode': 200,
            'body': 'Everything OK'
        }
        
