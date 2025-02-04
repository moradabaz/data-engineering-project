# Data Models

## Raw Data

### Amadeus

#### Metadata

- counts: Number of elements in data

#### Data

- type: No 
- id: No
- source: No
- instantTicketingRequired: No
- oneway: -> No
- itineraries:
    - duration -> La duración
    - segments -> array[dict]
        - Departure -> dict
            - iatcode -> Ciudad de salida
            - terminal
            - at -> fecha salida
        - Arrival
            - iatacode: Amsterdam
            - at -> fecha llegada
        - CarrieCode -> Nombre de compañia
        - Numero
        - Aircraft
            - code
        - operating (La compañia filial)
            - carrierCode
        - numberOfStops (Numero de paradas)
    - precios
        - currency
        - total
        - additionalServices (por ejemplo, facturar maletas)
            - amount
            - type -> (Checked_bags)
        - priceOptions
            - IncludedCheckedBagsOnly: Si incluye o no maletas facturadas
        - travelerPricings
            - fareDetailsBySegment
                - segmentId -> No interesa
                - cabin: Tipo de tarifa (Economica, turista)
                - brandedFare: Marga de la tarifa (Lite)
                - class: Clase
                - includedCheckedBags.quantity -> Maletas facturadas
 
#### Información relevante a extraer

*Origen - Destino - Fecha* 

- Tabla `Itinerario` 

id = MAD-AMS-20240403-1


- Tabla de `precios`


#### Dictionaries

*Create table for that contains countries and aircrafts*

- Locations -> [dict]
    - Country 
        - city Code -> MAD
        - country code -> ES
    - Aircraft -> [dict]
        - ID -> Aircraft Name
    - Currencies -> dict
        - the currency
    - Carriers (Compañía)
        - ID -> Company name

### Skyscanner

#### Metadata (filterStats)

- duration (minutes)
    - min
    - max
- airports
    - city
    - airports
        - id
        - entityId
        - name
    - carrier
        - name

#### Data

- price -> [ ]
    - raw
    - formatted
- legs -> [ ]
    - origin -> [ ]
        - id (MAD) => legs[0]["origin"]
        - name (Madrid)
        - displayCode (MAD)
        - city
        - country
    - destination -> []
        - name: airport name
        - city
        - displayCode
        - country
    - durationInMinutes: 155
    - stopCount: numero de paradas
    - departure: Departure Datetime
    - arrival: Arrival Datetime
    - timeDeltaInDays: Number of days
    - carriers:
        - marketing -> []
            - name
        - operationType (fully_operated)
    - segments -> []
        - origin -> []
            - flightPlaceId (MAD)
            - displayCode (MAD)
            - parent -> []
                - name
                - displayCode
                - type: City
            - name: (Madrid)
            - type: (Airport)
        - destination -> []
            - displayCode
            - parent -> []
                - displayCode
                - name 
                - type
            - departure: departure dattime
            - arrival: arrivaldatime
            - marketinCarrier -> []
                - name (Air Europa)
                - alternateId (UX)
            - operatintCarrier:
                - name (Air Europa)
                - alternateId (UX)
            - farePolicy -> []
                - isChangeAllowed
                - isPartiallyChangeable
                - isCancellationAllowed
                - isPartiallyRefundable
            - hasFlexibleOptions