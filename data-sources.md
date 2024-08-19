## Posible comparativa de precios e informacion de vuelos


### Amadeus ¿Que nos ofrece la API de amadeus?

- Flight Inspiration -> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-inspiration-search/api-reference
  - Frecuencia: Semanal
  - Descripcion: Información de posibles destinos junto con los vuelos mas baratos en una fecha especifica
  - Podemos elegir ida y vuelva o solo dia
- Flight Cheapest Search -> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-cheapest-date-search

Igual me interesa -> fechas, precio, tasas, informacion del avion

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

## Example

Quiero obtener sugerencias de vuelos desde Madrid

`GET https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD`

options

```
"defaults": {
      "departureDate": "2024-07-27,2025-01-22",
      "oneWay": false,
      "duration": "1,15",
      "nonStop": false,
      "viewBy": "DESTINATION"
    }
```

Result:

```
{
  "data": [
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "OPO",
      "departureDate": "2024-11-02",
      "returnDate": "2024-11-09",
      "price": {
        "total": "44.03"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=OPO&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=OPO&departureDate=2024-11-02&returnDate=2024-11-09&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "PMI",
      "departureDate": "2024-10-21",
      "returnDate": "2024-11-05",
      "price": {
        "total": "56.49"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=PMI&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=PMI&departureDate=2024-10-21&returnDate=2024-11-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "RAK",
      "departureDate": "2024-09-19",
      "returnDate": "2024-10-04",
      "price": {
        "total": "69.93"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=RAK&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=RAK&departureDate=2024-09-19&returnDate=2024-10-04&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LPA",
      "departureDate": "2024-11-28",
      "returnDate": "2024-12-13",
      "price": {
        "total": "74.89"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LPA&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LPA&departureDate=2024-11-28&returnDate=2024-12-13&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LIS",
      "departureDate": "2024-09-04",
      "returnDate": "2024-09-19",
      "price": {
        "total": "83.41"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LIS&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LIS&departureDate=2024-09-04&returnDate=2024-09-19&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LGW",
      "departureDate": "2024-11-13",
      "returnDate": "2024-11-26",
      "price": {
        "total": "84.24"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LGW&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LGW&departureDate=2024-11-13&returnDate=2024-11-26&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "FCO",
      "departureDate": "2024-11-19",
      "returnDate": "2024-11-30",
      "price": {
        "total": "89.36"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=FCO&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=FCO&departureDate=2024-11-19&returnDate=2024-11-30&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "ORY",
      "departureDate": "2024-08-07",
      "returnDate": "2024-08-22",
      "price": {
        "total": "92.19"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=ORY&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=ORY&departureDate=2024-08-07&returnDate=2024-08-22&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MXP",
      "departureDate": "2024-08-15",
      "returnDate": "2024-08-26",
      "price": {
        "total": "104.03"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MXP&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MXP&departureDate=2024-08-15&returnDate=2024-08-26&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "AMS",
      "departureDate": "2024-11-13",
      "returnDate": "2024-11-14",
      "price": {
        "total": "124.08"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=AMS&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=AMS&departureDate=2024-11-13&returnDate=2024-11-14&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "EWR",
      "departureDate": "2024-11-21",
      "returnDate": "2024-12-05",
      "price": {
        "total": "364.37"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=EWR&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=EWR&departureDate=2024-11-21&returnDate=2024-12-05&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "MIA",
      "departureDate": "2024-10-09",
      "returnDate": "2024-10-20",
      "price": {
        "total": "428.51"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MIA&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=MIA&departureDate=2024-10-09&returnDate=2024-10-20&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "BKK",
      "departureDate": "2024-09-23",
      "returnDate": "2024-10-02",
      "price": {
        "total": "499.71"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=BKK&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BKK&departureDate=2024-09-23&returnDate=2024-10-02&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "CUN",
      "departureDate": "2025-01-15",
      "returnDate": "2025-01-24",
      "price": {
        "total": "529.64"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=CUN&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=CUN&departureDate=2025-01-15&returnDate=2025-01-24&adults=1&nonStop=false"
      }
    },
    {
      "type": "flight-destination",
      "origin": "MAD",
      "destination": "LAX",
      "departureDate": "2024-09-05",
      "returnDate": "2024-09-08",
      "price": {
        "total": "545.80"
      },
      "links": {
        "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=LAX&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=LAX&departureDate=2024-09-05&returnDate=2024-09-08&adults=1&nonStop=false"
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
      "PMI": {
        "subType": "AIRPORT",
        "detailedName": "PALMA DE MALLORCA"
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
      "self": "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&departureDate=2024-07-27,2025-01-22&oneWay=false&duration=1,15&nonStop=false&viewBy=DESTINATION"
    },
    "defaults": {
      "departureDate": "2024-07-27,2025-01-22",
      "oneWay": false,
      "duration": "1,15",
      "nonStop": false,
      "viewBy": "DESTINATION"
    }
  }
}
```

Nos interesa el vuelo de Madrid-Marrakech el dia 19-09-2024


`GET  https://sky-scanner3.p.rapidapi.com/flights/search-one-way?fromEntityId=MAD&toEntityId=RAK&departDate=2024-09-19&cabinClass=economy`

```
{
    "data": {
        "context": {
            "status": "incomplete",
            "sessionId": "ClQIARJQCk4KJDY5OTk0OTAzLTdlZTgtNDU4Mi1hZjE2LWMwNmQ4NWJhZjVkYRACGiRmNTZiOWQ4YS05YzkwLTQ0YTctYjExOS1hNzc0ZWE3MmE1MTQSKHVzc182MDI5OTZjNy0yZjcyLTQ2NzktYWJjNS0yNTQzOTA0N2YxYTI=",
            "totalResults": 10
        },
        "itineraries": [
            {
                "id": "13870-2409191535--31915-0-15753-2409191640",
                "price": {
                    "raw": 29.16,
                    "formatted": "$30",
                    "pricingOptionId": "uZ0ILj-ZF2ag"
                },
                "legs": [
                    {
                        "id": "13870-2409191535--31915-0-15753-2409191640",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 125,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T15:35:00",
                        "arrival": "2024-09-19T16:40:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -31915,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/FR.png",
                                    "name": "Ryanair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191535-2409191640--31915",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T15:35:00",
                                "arrival": "2024-09-19T16:40:00",
                                "durationInMinutes": 125,
                                "flightNumber": "6791",
                                "marketingCarrier": {
                                    "id": -31915,
                                    "name": "Ryanair",
                                    "alternateId": "FR",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -31915,
                                    "name": "Ryanair",
                                    "alternateId": "FR",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "tags": [
                    "cheapest"
                ],
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.999
            },
            {
                "id": "13870-2409191315--31915-0-15753-2409191420",
                "price": {
                    "raw": 33.71,
                    "formatted": "$34",
                    "pricingOptionId": "8ZYiEfu4I5hi"
                },
                "legs": [
                    {
                        "id": "13870-2409191315--31915-0-15753-2409191420",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 125,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T13:15:00",
                        "arrival": "2024-09-19T14:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -31915,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/FR.png",
                                    "name": "Ryanair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191315-2409191420--31915",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T13:15:00",
                                "arrival": "2024-09-19T14:20:00",
                                "durationInMinutes": 125,
                                "flightNumber": "6721",
                                "marketingCarrier": {
                                    "id": -31915,
                                    "name": "Ryanair",
                                    "alternateId": "FR",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -31915,
                                    "name": "Ryanair",
                                    "alternateId": "FR",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "tags": [
                    "second_cheapest"
                ],
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.956693
            },
            {
                "id": "13870-2409192350--32680-0-15753-2409200055",
                "price": {
                    "raw": 38.62,
                    "formatted": "$39",
                    "pricingOptionId": "Jri8aiV9G97H"
                },
                "legs": [
                    {
                        "id": "13870-2409192350--32680-0-15753-2409200055",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 125,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T23:50:00",
                        "arrival": "2024-09-20T00:55:00",
                        "timeDeltaInDays": 1,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32680,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/UX.png",
                                    "name": "Air Europa"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409192350-2409200055--32680",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T23:50:00",
                                "arrival": "2024-09-20T00:55:00",
                                "durationInMinutes": 125,
                                "flightNumber": "1423",
                                "marketingCarrier": {
                                    "id": -32680,
                                    "name": "Air Europa",
                                    "alternateId": "UX",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32680,
                                    "name": "Air Europa",
                                    "alternateId": "UX",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "tags": [
                    "third_cheapest"
                ],
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.601843
            },
            {
                "id": "13870-2409191550--32221-0-15753-2409191655",
                "price": {
                    "raw": 83.68,
                    "formatted": "$84",
                    "pricingOptionId": "S_7-smoXmEjm"
                },
                "legs": [
                    {
                        "id": "13870-2409191550--32221-0-15753-2409191655",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 125,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T15:50:00",
                        "arrival": "2024-09-19T16:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32221,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                                    "name": "Iberia Express"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191550-2409191655--32221",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T15:50:00",
                                "arrival": "2024-09-19T16:55:00",
                                "durationInMinutes": 125,
                                "flightNumber": "3622",
                                "marketingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.506018
            },
            {
                "id": "13870-2409191550--32222-0-15753-2409191655",
                "price": {
                    "raw": 83.12,
                    "formatted": "$84",
                    "pricingOptionId": "SQThdaKV2rhS"
                },
                "legs": [
                    {
                        "id": "13870-2409191550--32222-0-15753-2409191655",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 125,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T15:50:00",
                        "arrival": "2024-09-19T16:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/IB.png",
                                    "name": "Iberia"
                                }
                            ],
                            "operating": [
                                {
                                    "id": -32221,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                                    "name": "Iberia Express"
                                }
                            ],
                            "operationType": "not_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191550-2409191655--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T15:50:00",
                                "arrival": "2024-09-19T16:55:00",
                                "durationInMinutes": 125,
                                "flightNumber": "3622",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternateId": "IB",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.503212
            },
            {
                "id": "13870-2409191015--32221-0-15753-2409191115",
                "price": {
                    "raw": 91.59,
                    "formatted": "$92",
                    "pricingOptionId": "xOi7hRp_Y4Us"
                },
                "legs": [
                    {
                        "id": "13870-2409191015--32221-0-15753-2409191115",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 120,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T10:15:00",
                        "arrival": "2024-09-19T11:15:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32221,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                                    "name": "Iberia Express"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191015-2409191115--32221",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T10:15:00",
                                "arrival": "2024-09-19T11:15:00",
                                "durationInMinutes": 120,
                                "flightNumber": "3620",
                                "marketingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "tags": [
                    "shortest"
                ],
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.489368
            },
            {
                "id": "13870-2409191015--32222-0-15753-2409191115",
                "price": {
                    "raw": 97.23,
                    "formatted": "$98",
                    "pricingOptionId": "WvrMv998yNWf"
                },
                "legs": [
                    {
                        "id": "13870-2409191015--32222-0-15753-2409191115",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 120,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T10:15:00",
                        "arrival": "2024-09-19T11:15:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/IB.png",
                                    "name": "Iberia"
                                }
                            ],
                            "operating": [
                                {
                                    "id": -32221,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                                    "name": "Iberia Express"
                                }
                            ],
                            "operationType": "not_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191015-2409191115--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T10:15:00",
                                "arrival": "2024-09-19T11:15:00",
                                "durationInMinutes": 120,
                                "flightNumber": "3620",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternateId": "IB",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "tags": [
                    "second_shortest"
                ],
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.462459
            },
            {
                "id": "13870-2409191550--31927-0-15753-2409191655",
                "price": {
                    "raw": 158.08,
                    "formatted": "$159",
                    "pricingOptionId": "nTEp7Xu5o9Ej"
                },
                "legs": [
                    {
                        "id": "13870-2409191550--31927-0-15753-2409191655",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 125,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T15:50:00",
                        "arrival": "2024-09-19T16:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -31927,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/AT.png",
                                    "name": "Royal Air Maroc"
                                }
                            ],
                            "operating": [
                                {
                                    "id": -32221,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                                    "name": "Iberia Express"
                                }
                            ],
                            "operationType": "not_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191550-2409191655--31927",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T15:50:00",
                                "arrival": "2024-09-19T16:55:00",
                                "durationInMinutes": 125,
                                "flightNumber": "5306",
                                "marketingCarrier": {
                                    "id": -31927,
                                    "name": "Royal Air Maroc",
                                    "alternateId": "AT",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.359818
            },
            {
                "id": "13870-2409191015--31927-0-15753-2409191115",
                "price": {
                    "raw": 206.92,
                    "formatted": "$207",
                    "pricingOptionId": "kBHOfeLEEbMP"
                },
                "legs": [
                    {
                        "id": "13870-2409191015--31927-0-15753-2409191115",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 120,
                        "stopCount": 0,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T10:15:00",
                        "arrival": "2024-09-19T11:15:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -31927,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/AT.png",
                                    "name": "Royal Air Maroc"
                                }
                            ],
                            "operating": [
                                {
                                    "id": -32221,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                                    "name": "Iberia Express"
                                }
                            ],
                            "operationType": "not_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-15753-2409191015-2409191115--31927",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T10:15:00",
                                "arrival": "2024-09-19T11:15:00",
                                "durationInMinutes": 120,
                                "flightNumber": "5304",
                                "marketingCarrier": {
                                    "id": -31927,
                                    "name": "Royal Air Maroc",
                                    "alternateId": "AT",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -32221,
                                    "name": "Iberia Express",
                                    "alternateId": "I2",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "tags": [
                    "third_shortest"
                ],
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.326574
            },
            {
                "id": "13870-2409191935--31927-1-15753-2409192255",
                "price": {
                    "raw": 145.85,
                    "formatted": "$146",
                    "pricingOptionId": "erMBCUGf9onK"
                },
                "legs": [
                    {
                        "id": "13870-2409191935--31927-1-15753-2409192255",
                        "origin": {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid",
                            "displayCode": "MAD",
                            "city": "Madrid",
                            "country": "Spain",
                            "isHighlighted": false
                        },
                        "destination": {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara",
                            "displayCode": "RAK",
                            "city": "Marrakech",
                            "country": "Morocco",
                            "isHighlighted": false
                        },
                        "durationInMinutes": 260,
                        "stopCount": 1,
                        "isSmallestStops": false,
                        "departure": "2024-09-19T19:35:00",
                        "arrival": "2024-09-19T22:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -31927,
                                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/AT.png",
                                    "name": "Royal Air Maroc"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-10622-2409191935-2409192025--31927",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "displayCode": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MADR",
                                        "displayCode": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport",
                                    "country": "Spain"
                                },
                                "destination": {
                                    "flightPlaceId": "CMN",
                                    "displayCode": "CMN",
                                    "parent": {
                                        "flightPlaceId": "CASA",
                                        "displayCode": "CAS",
                                        "name": "Casablanca",
                                        "type": "City"
                                    },
                                    "name": "Casablanca Mohamed V.",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T19:35:00",
                                "arrival": "2024-09-19T20:25:00",
                                "durationInMinutes": 110,
                                "flightNumber": "971",
                                "marketingCarrier": {
                                    "id": -31927,
                                    "name": "Royal Air Maroc",
                                    "alternateId": "AT",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -31927,
                                    "name": "Royal Air Maroc",
                                    "alternateId": "AT",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            },
                            {
                                "id": "10622-15753-2409192150-2409192255--31927",
                                "origin": {
                                    "flightPlaceId": "CMN",
                                    "displayCode": "CMN",
                                    "parent": {
                                        "flightPlaceId": "CASA",
                                        "displayCode": "CAS",
                                        "name": "Casablanca",
                                        "type": "City"
                                    },
                                    "name": "Casablanca Mohamed V.",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "destination": {
                                    "flightPlaceId": "RAK",
                                    "displayCode": "RAK",
                                    "parent": {
                                        "flightPlaceId": "MARR",
                                        "displayCode": "RAK",
                                        "name": "Marrakech",
                                        "type": "City"
                                    },
                                    "name": "Marrakech Menara",
                                    "type": "Airport",
                                    "country": "Morocco"
                                },
                                "departure": "2024-09-19T21:50:00",
                                "arrival": "2024-09-19T22:55:00",
                                "durationInMinutes": 65,
                                "flightNumber": "401",
                                "marketingCarrier": {
                                    "id": -31927,
                                    "name": "Royal Air Maroc",
                                    "alternateId": "AT",
                                    "allianceId": 0,
                                    "displayCode": ""
                                },
                                "operatingCarrier": {
                                    "id": -31927,
                                    "name": "Royal Air Maroc",
                                    "alternateId": "AT",
                                    "allianceId": 0,
                                    "displayCode": ""
                                }
                            }
                        ]
                    }
                ],
                "isSelfTransfer": false,
                "isProtectedSelfTransfer": false,
                "farePolicy": {
                    "isChangeAllowed": false,
                    "isPartiallyChangeable": false,
                    "isCancellationAllowed": false,
                    "isPartiallyRefundable": false
                },
                "fareAttributes": {},
                "isMashUp": false,
                "hasFlexibleOptions": false,
                "score": 0.232141
            }
        ],
        "messages": [],
        "filterStats": {
            "duration": {
                "min": 120,
                "max": 260,
                "multiCityMin": 120,
                "multiCityMax": 260
            },
            "airports": [
                {
                    "city": "Madrid",
                    "airports": [
                        {
                            "id": "MAD",
                            "entityId": "95565077",
                            "name": "Madrid"
                        }
                    ]
                },
                {
                    "city": "Marrakech",
                    "airports": [
                        {
                            "id": "RAK",
                            "entityId": "95673588",
                            "name": "Marrakech Menara"
                        }
                    ]
                }
            ],
            "carriers": [
                {
                    "id": -32680,
                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/UX.png",
                    "name": "Air Europa"
                },
                {
                    "id": -32222,
                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/IB.png",
                    "name": "Iberia"
                },
                {
                    "id": -32221,
                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/I2.png",
                    "name": "Iberia Express"
                },
                {
                    "id": -31927,
                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/AT.png",
                    "name": "Royal Air Maroc"
                },
                {
                    "id": -31915,
                    "logoUrl": "https://logos.skyscnr.com/images/airlines/favicon/FR.png",
                    "name": "Ryanair"
                }
            ],
            "stopPrices": {
                "direct": {
                    "isPresent": true,
                    "formattedPrice": "$30"
                },
                "one": {
                    "isPresent": true,
                    "formattedPrice": "$146"
                },
                "twoOrMore": {
                    "isPresent": false
                }
            }
        },
        "flightsSessionId": "69994903-7ee8-4582-af16-c06d85baf5da",
        "destinationImageUrl": "https://content.skyscnr.com/m/3719e8f4a5daf43d/original/Flights-Placeholder.jpg",
        "token": "eyJhIjoxLCJjIjowLCJpIjowLCJjYyI6ImVjb25vbXkiLCJvIjoiTUFEIiwiZCI6IlJBSyIsImQxIjoiMjAyNC0wOS0xOSJ9"
    },
    "status": true,
    "message": "Successful"
}
```
