import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from pyspark.sql.functions import col, explode, date_format, concat, lit, regexp_replace
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

dyf = glueContext.create_dynamic_frame.from_catalog(database='raw-skyscanner-db', table_name='skyscanner')

df = dyf.toDF()

itineraries_df = df.selectExpr(
    "ori",
    "dest",
    "dest",
    "year",
    "month",
    "week",
    "day",
    "data.itineraries"
    )


itineraries_df = itineraries_df.withColumn("itinerary", explode(col("itineraries")))


from pyspark.sql.functions import col, explode

# Seleccionar columnas relevantes del itinerario
details_df = itineraries_df.select(
    "ori", "dest", "year", "month", "week", "day",
    col("itinerary.price.raw").alias("price_raw"),
    col("itinerary.legs").alias("legs"),
    col("itinerary.farePolicy").alias("farePolicy"),
    col("itinerary.isSelfTransfer").alias("isSelfTransfer"),
    col("itinerary.isProtectedSelfTransfer").alias("isProtectedSelfTransfer")
)

# Explotar legs para dividir los vuelos en filas individuales
legs_df = details_df.withColumn("leg", explode("legs")) \
    .withColumn("marketing", explode("leg.carriers.marketing")) \
    .withColumn("segments", explode("leg.segments"))

# Definir columnas finales de salida
selected_columns = [
    "ori", "dest", "year", "month", "week", "day", "price_raw",
    col("leg.id").alias("leg_id"),
    col("leg.origin.name").alias("origin_name"),
    col("leg.origin.displayCode").alias("origin_airport"),
    col("leg.origin.city").alias("origin_city"),
    col("leg.origin.country").alias("origin_country"),
    col("leg.destination.name").alias("destination_name"),
    col("leg.destination.displayCode").alias("destination_airport"),
    col("leg.destination.city").alias("destination_city"),
    col("leg.destination.country").alias("destination_country"),
    col("leg.durationInMinutes").alias("duration_in_minutes"),
    col("leg.isSmallestStops").alias("is_smallest_stops"),
    col("leg.timeDeltaInDays").alias("time_delta_days"),
    col("leg.departure").alias("departure_time"),
    col("leg.arrival").alias("arrival_time"),
    col("leg.carriers.operationType").alias("company_operation_type"),
    col("segments.flightNumber").alias("flight_number"),
    col("segments.marketingCarrier.name").alias("marketing_company_name"),
    col("segments.marketingCarrier.alternateId").alias("marketing_company_code"),
    col("segments.operatingCarrier.name").alias("operating_company_name"),
    col("segments.operatingCarrier.alternateId").alias("operating_company_code"),
    col("isSelfTransfer"),
    col("isProtectedSelfTransfer"),
    col("farePolicy.isChangeAllowed"),
    col("farePolicy.isPartiallyChangeable"),
    col("farePolicy.isCancellationAllowed"),
    col("farePolicy.isPartiallyRefundable")
]

# Crear el DataFrame final con los datos limpios y estructurados
final_legs_df = legs_df.select(*selected_columns)

# Guardar en formato parquet en S3 (descomentar si es necesario)
output_flights_path = "s3://my-aws-project-v1/transformed/skyscanner/flights"
final_legs_df.write.format("parquet").mode("overwrite").partitionBy("ori", "dest", "year", "month", "week", "day").save(output_flights_path)
