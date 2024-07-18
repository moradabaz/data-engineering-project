# data-engineering-project
Data engineering using cloud tools for turism data management

### Pasos para Crear un Data Pipeline

1. **Definición de Objetivos y Requerimientos**
    - **Objetivo**: Crear un pipeline de datos que recolecte y procese información sobre turismo, vuelos, alquileres de vehículos y alojamientos.
    - **Requerimientos**: Seleccionar APIs, herramientas de ingestión, orquestación, almacenamiento y visualización.

2. **Selección de APIs**
    - **Amadeus API**: Para datos de vuelos, hoteles y alquileres de vehículos.
    - **Skyscanner API**: Para datos de vuelos.
    - **INE API**: Para estadísticas de turismo.

3. **Ingestión de Datos**
    - **Herramienta**: Python
    - **Proceso**:
        1. Escribir scripts en Python para recolectar datos de las APIs.
        2. Guardar los datos crudos en Amazon S3 para almacenamiento intermedio.

4. **Almacenamiento Intermedio**
    - **Herramienta**: Amazon S3
    - **Proceso**: Subir los datos recolectados en formato JSON o CSV a un bucket de S3.

5. **Orquestación y Automatización**
    - **Herramienta**: Apache Airflow
    - **Proceso**:
        1. Configurar DAGs (Directed Acyclic Graphs) en Airflow para automatizar la ingestión de datos desde las APIs y su almacenamiento en S3.
        2. Programar tareas para la transformación de datos.

6. **Transformación de Datos**
    - **Herramienta**: DBT (Data Build Tool)
    - **Proceso**:
        1. Crear modelos en DBT para limpiar y transformar los datos almacenados en S3.
        2. Generar tablas maestras con los datos procesados.

7. **Carga de Datos a PostgreSQL**
    - **Herramienta**: Python y/o Airflow
    - **Proceso**:
        1. Escribir scripts en Python o tareas en Airflow para cargar los datos transformados desde S3 a PostgreSQL.
        2. Utilizar librerías como `psycopg2` para la conexión y carga de datos a PostgreSQL.

8. **Almacenamiento Final**
    - **Herramienta**: PostgreSQL
    - **Proceso**: Crear tablas en PostgreSQL para almacenar los datos transformados.

9. **Visualización de Datos**
    - **Herramientas**: Tableau, Power BI o cualquier herramienta de BI que prefieras
    - **Proceso**:
        1. Conectar la herramienta de BI a PostgreSQL.
        2. Crear dashboards y visualizaciones basadas en las tablas maestras.

### Ejemplo de Estructura de Tablas Maestras

#### Tabla de Visitantes
- `visitor_id`: Identificador único del visitante.
- `visit_date`: Fecha de la visita.
- `origin_country`: País de origen del visitante.
- `destination_city`: Ciudad de destino.
- `transport_mode`: Modo de transporte (avión, coche, etc.).

#### Tabla de Vuelos
- `flight_id`: Identificador único del vuelo.
- `visitor_id`: Identificador único del visitante.
- `flight_date`: Fecha del vuelo.
- `origin_airport`: Aeropuerto de origen.
- `destination_airport`: Aeropuerto de destino.
- `airline`: Aerolínea.

#### Tabla de Hoteles
- `hotel_id`: Identificador único del hotel.
- `visitor_id`: Identificador único del visitante.
- `hotel_name`: Nombre del hotel.
- `check_in_date`: Fecha de check-in.
- `check_out_date`: Fecha de check-out.
- `city`: Ciudad del hotel.

#### Tabla de Alquileres de Vehículos
- `rental_id`: Identificador único del alquiler.
- `visitor_id`: Identificador único del visitante.
- `rental_date`: Fecha del alquiler.
- `return_date`: Fecha de devolución.
- `pickup_location`: Lugar de recogida.
- `dropoff_location`: Lugar de devolución.
- `car_type`: Tipo de coche.

### Resumen del Pipeline

1. **Ingestión de Datos**: Scripts en Python para recolectar datos de APIs y almacenar en S3.
2. **Almacenamiento Intermedio**: Amazon S3 para almacenamiento de datos crudos.
3. **Orquestación y Automatización**: Airflow para automatizar la ingestión y transformación de datos.
4. **Transformación de Datos**: DBT para limpiar y transformar los datos.
5. **Carga de Datos**: Scripts en Python para cargar datos transformados desde S3 a PostgreSQL.
6. **Almacenamiento Final**: PostgreSQL para almacenamiento de datos estructurados.
7. **Visualización**: Herramientas de BI conectadas a PostgreSQL para crear dashboards.

Este enfoque te permitirá construir un pipeline de datos eficiente y escalable, utilizando herramientas modernas y accesibles.
