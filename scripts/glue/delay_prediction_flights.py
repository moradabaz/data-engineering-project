import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from pyspark.sql.functions import col, explode

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

dyf = glueContext.create_dynamic_frame.from_catalog(database='raw-amadeus-db', table_name='delays-rawflight_delays')

df = dyf.toDF()

output_path = "s3://my-aws-project-v1/transformed/predictions/"  # 📂 Carpeta de salida


df_exploded = df.withColumn("prediction", explode(col("prediction_data")))

df_flattened = df_exploded.select(
    # Datos de vuelo
    col("flight_data.departure_date").substr(1, 4).alias("year"),
    col("flight_data.departure_date").substr(6, 2).alias("month"),
    col("flight_data.departure_date").substr(9, 2).alias("day"),
    col("flight_data.departure").alias("departure_airport"),
    col("flight_data.arrival").alias("arrival_airport"),
    col("flight_data.departure_date").alias("departure_date"),
    col("flight_data.departure_time").alias("departure_time"),
    col("flight_data.arrival_date").alias("arrival_date"),
    col("flight_data.arrival_time").alias("arrival_time"),
    col("flight_data.aircraft_code").alias("aircraft_code"),
    col("flight_data.carrier").alias("carrier"),
    col("flight_data.flight_number").alias("flight_number"),
    col("flight_data.flight_duration").alias("flight_duration"),
    col("prediction.probability").alias("delay_probability"),
    col("prediction.result").alias("delay_result"),
    col("prediction.subType").alias("sub_type"),
    col("prediction.type").alias("type")
)

df_flattened.write.format("parquet").mode("append").partitionBy("year", "month", "day").save(output_path)

job.commit()