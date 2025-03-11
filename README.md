# Data Engineering Project
Data engineering using cloud tools for turism data management

## General Architecture (To be done)

![image](https://github.com/user-attachments/assets/067bf94b-b603-4625-9106-c126a90b6142)


## Steps

### Extract data from amadeus and Skyscanner

![alt text](image-1.png)

### Resumen del Pipeline

1. **Ingestión de Datos**: Scripts en Python para recolectar datos de APIs y almacenar en S3.
2. **Almacenamiento Intermedio**: Amazon S3 para almacenamiento de datos crudos.
3. **Orquestación y Automatización**: Airflow para automatizar la ingestión y transformación de datos.
4. **Transformación de Datos**: DBT para limpiar y transformar los datos.
5. **Carga de Datos**: Scripts en Python para cargar datos transformados desde S3 a PostgreSQL.
6. **Almacenamiento Final**: PostgreSQL para almacenamiento de datos estructurados.
7. **Visualización**: Herramientas de BI conectadas a PostgreSQL para crear dashboards.

Este enfoque te permitirá construir un pipeline de datos eficiente y escalable, utilizando herramientas modernas y accesibles.



