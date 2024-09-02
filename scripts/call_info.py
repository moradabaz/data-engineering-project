import json
import os

print(os.getcwd() + '/response_data.json')
f = open('/home/morad/data-engineering-project/scripts/response_data.json')
data = json.load(f)

for flights in data['data']:
    print(flights['links']['flightOffers'])
