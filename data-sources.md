## Posible comparativa de precios e informacion


### Amadeus ¿Que nos ofrece la API de amadeus?

- Flight Inspiration -> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-inspiration-search/api-reference
  - Frecuencia: Semanal
  - Descripcion: Información de posibles destinos junto con los vuelos mas baratos en una fecha especifica
  - Podemos elegir ida y vuelva o solo dia
- Flight Cheapest Search -> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-cheapest-date-search
  - 

### Skyscanner API (Rapidapi)

#### What kind of information do we need?

1. We will to search for the spanish destiny airports (MAD, BCN, VLC, PMA, MAL, etc)

##### Top 3 visited cities of the most visited countries in Europe

1. France
  - Paris
  - Nice
  - Cannes

2. Spain
   - Barcelona
   - Madrid
   - Palma de Mallorca

3. Italy
   - Rome
   - Venice
   - Italy

4. United Kingdome
   - London
   - Edimburgh
   - Manchester
  
5. Germany
   - Berlin
   - Munich
   - Hamburg
  
### The API endpoints we will use

1. Get inspirational flights for each of one of this 
2. Get The best prices for the week in which the suggested us to fly for round-trip or one-way (booking)
3. Get The best prices

### Example

Madrid 28/07 - 10/08

```
{
  "data": [
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LPA",
      "departureDate": "2024-07-28",
      "price": {
        "total": "225.41"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LPA&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LPA&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "JFK",
      "departureDate": "2024-07-28",
      "price": {
        "total": "726.24"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=JFK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=JFK&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "BCN",
      "departureDate": "2024-08-05",
      "price": {
        "total": "25.67"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=BCN&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BCN&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "PMI",
      "departureDate": "2024-08-05",
      "price": {
        "total": "117.65"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=PMI&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=PMI&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "JFK",
      "departureDate": "2024-08-05",
      "price": {
        "total": "827.21"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=JFK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=JFK&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "JFK",
      "departureDate": "2024-07-29",
      "price": {
        "total": "726.24"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=JFK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=JFK&departureDate=2024-07-29&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "ORY",
      "departureDate": "2024-07-30",
      "price": {
        "total": "55.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=ORY&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=ORY&departureDate=2024-07-30&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "ORY",
      "departureDate": "2024-07-28",
      "price": {
        "total": "85.95"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=ORY&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=ORY&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LPA",
      "departureDate": "2024-08-05",
      "price": {
        "total": "213.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LPA&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LPA&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "ORY",
      "departureDate": "2024-08-05",
      "price": {
        "total": "61.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=ORY&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=ORY&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LPA",
      "departureDate": "2024-07-29",
      "price": {
        "total": "200.11"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LPA&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LPA&departureDate=2024-07-29&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "PMI",
      "departureDate": "2024-07-29",
      "price": {
        "total": "70.65"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=PMI&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=PMI&departureDate=2024-07-29&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "EWR",
      "departureDate": "2024-07-31",
      "price": {
        "total": "830.79"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=EWR&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=EWR&departureDate=2024-07-31&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "PMI",
      "departureDate": "2024-07-28",
      "price": {
        "total": "93.65"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=PMI&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=PMI&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LHR",
      "departureDate": "2024-08-01",
      "price": {
        "total": "180.65"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LHR&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LHR&departureDate=2024-08-01&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "RAK",
      "departureDate": "2024-08-05",
      "price": {
        "total": "170.65"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=RAK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=RAK&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "RAK",
      "departureDate": "2024-07-28",
      "price": {
        "total": "220.57"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=RAK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=RAK&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "RAK",
      "departureDate": "2024-08-04",
      "price": {
        "total": "118.57"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=RAK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=RAK&departureDate=2024-08-04&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "BKK",
      "departureDate": "2024-08-05",
      "price": {
        "total": "681.55"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=BKK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BKK&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "FCO",
      "departureDate": "2024-08-05",
      "price": {
        "total": "155.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=FCO&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=FCO&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "FCO",
      "departureDate": "2024-07-31",
      "price": {
        "total": "103.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=FCO&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=FCO&departureDate=2024-07-31&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "BKK",
      "departureDate": "2024-07-28",
      "price": {
        "total": "791.55"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=BKK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BKK&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "FCO",
      "departureDate": "2024-07-28",
      "price": {
        "total": "118.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=FCO&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=FCO&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "BKK",
      "departureDate": "2024-07-30",
      "price": {
        "total": "681.55"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=BKK&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BKK&departureDate=2024-07-30&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LAX",
      "departureDate": "2024-08-05",
      "price": {
        "total": "1304.98"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LAX&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LAX&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LGW",
      "departureDate": "2024-08-05",
      "price": {
        "total": "197.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LGW&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LGW&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LAX",
      "departureDate": "2024-08-03",
      "price": {
        "total": "1269.60"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LAX&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LAX&departureDate=2024-08-03&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MIA",
      "departureDate": "2024-07-28",
      "price": {
        "total": "924.33"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MIA&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MIA&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LAX",
      "departureDate": "2024-07-28",
      "price": {
        "total": "1299.85"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LAX&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LAX&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MIA",
      "departureDate": "2024-08-05",
      "price": {
        "total": "1059.21"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MIA&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MIA&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MIA",
      "departureDate": "2024-07-30",
      "price": {
        "total": "894.21"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MIA&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MIA&departureDate=2024-07-30&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LGW",
      "departureDate": "2024-07-30",
      "price": {
        "total": "175.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LGW&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LGW&departureDate=2024-07-30&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LGW",
      "departureDate": "2024-07-28",
      "price": {
        "total": "153.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LGW&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LGW&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "AMS",
      "departureDate": "2024-07-28",
      "price": {
        "total": "122.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=AMS&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=AMS&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "AMS",
      "departureDate": "2024-07-31",
      "price": {
        "total": "122.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=AMS&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=AMS&departureDate=2024-07-31&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MXP",
      "departureDate": "2024-07-28",
      "price": {
        "total": "105.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MXP&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MXP&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "AMS",
      "departureDate": "2024-08-05",
      "price": {
        "total": "144.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=AMS&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=AMS&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MXP",
      "departureDate": "2024-07-29",
      "price": {
        "total": "81.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MXP&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MXP&departureDate=2024-07-29&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MXP",
      "departureDate": "2024-08-05",
      "price": {
        "total": "105.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MXP&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MXP&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "OPO",
      "departureDate": "2024-08-05",
      "price": {
        "total": "126.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=OPO&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=OPO&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "OPO",
      "departureDate": "2024-07-28",
      "price": {
        "total": "132.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=OPO&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=OPO&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "OPO",
      "departureDate": "2024-07-31",
      "price": {
        "total": "84.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=OPO&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=OPO&departureDate=2024-07-31&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "CUN",
      "departureDate": "2024-07-28",
      "price": {
        "total": "971.96"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=CUN&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=CUN&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "CUN",
      "departureDate": "2024-07-30",
      "price": {
        "total": "797.08"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=CUN&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=CUN&departureDate=2024-07-30&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "CUN",
      "departureDate": "2024-08-05",
      "price": {
        "total": "1027.10"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=CUN&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=CUN&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LIS",
      "departureDate": "2024-08-05",
      "price": {
        "total": "127.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LIS&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LIS&departureDate=2024-08-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LIS",
      "departureDate": "2024-07-28",
      "price": {
        "total": "92.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LIS&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LIS&departureDate=2024-07-28&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LIS",
      "departureDate": "2024-08-04",
      "price": {
        "total": "87.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LIS&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LIS&departureDate=2024-08-04&adults=1&nonStop=false"
      }
    }
  ],
  "dictionaries": {
    "currencies": {
      "EUR": "EURO"
    },
    "locations": {
      "EWR": {
        "subType": "AIRPORT",
        "detailedName": "NEWARK LIBERTY INTL"
      },
      "LAX": {
        "subType": "AIRPORT",
        "detailedName": "LOS ANGELES INTL"
      },
      "BKK": {
        "subType": "AIRPORT",
        "detailedName": "SUVARNABHUMI INTL"
      },
      "MIA": {
        "subType": "AIRPORT",
        "detailedName": "MIAMI INTL"
      },
      "MXP": {
        "subType": "AIRPORT",
        "detailedName": "MALPENSA"
      },
      "AMS": {
        "subType": "AIRPORT",
        "detailedName": "SCHIPHOL AIRPORT"
      },
      "BCN": {
        "subType": "AIRPORT",
        "detailedName": "AIRPORT"
      },
      "PMI": {
        "subType": "AIRPORT",
        "detailedName": "PALMA DE MALLORCA"
      },
      "JFK": {
        "subType": "AIRPORT",
        "detailedName": "JOHN F KENNEDY INTL"
      },
      "OPO": {
        "subType": "AIRPORT",
        "detailedName": "FRANCISCO SA CARNEIRO"
      },
      "MAD": {
        "subType": "AIRPORT",
        "detailedName": "ADOLFO SUAREZ BARAJAS"
      },
      "FCO": {
        "subType": "AIRPORT",
        "detailedName": "FIUMICINO"
      },
      "ORY": {
        "subType": "AIRPORT",
        "detailedName": "ORLY"
      },
      "LHR": {
        "subType": "AIRPORT",
        "detailedName": "HEATHROW"
      },
      "LIS": {
        "subType": "AIRPORT",
        "detailedName": "AIRPORT"
      },
      "LPA": {
        "subType": "AIRPORT",
        "detailedName": "GRAN CANARIA"
      },
      "LGW": {
        "subType": "AIRPORT",
        "detailedName": "GATWICK"
      },
      "CUN": {
        "subType": "AIRPORT",
        "detailedName": "INTERNATIONAL"
      },
      "RAK": {
        "subType": "AIRPORT",
        "detailedName": "MENARA"
      }
    }
  },
  "meta": {
    "currency": "EUR",
    "links": {
      "self": "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&departureDate=2024-07-28,2024-08-05&oneWay=true&nonStop=false&viewBy=WEEK"
    }
  }
}
```


