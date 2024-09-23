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

dyf = glueContext.create_dynamic_frame.from_catalog(database='raw-amadeus-db', table_name='amadeus')

df = dyf.toDF()

extracted_df = df.selectExpr("explode(data) as flight_offer").selectExpr(
    "flight_offer.id as flight_id",
    "flight_offer.itineraries[0].segments[0].departure.iataCode as departure_airport",
    "flight_offer.itineraries[0].segments[0].departure.at as departure_time",
    "flight_offer.itineraries[0].segments[0].departure.terminal as departure_terminal",
    "flight_offer.itineraries[0].segments[0].arrival.iataCode as arrival_airport",
    "flight_offer.itineraries[0].segments[0].arrival.at as arrival_time",
    "flight_offer.itineraries[0].segments[0].carrierCode as carrier",
    "flight_offer.itineraries[0].segments[0].number as flight_number",
    "flight_offer.itineraries[0].segments[0].aircraft.code as aircraft_code",
    "flight_offer.itineraries[0].segments[0].operating.carrierCode as company_code",
    "flight_offer.itineraries[0].segments[0].duration as flight_duration",
    "flight_offer.itineraries[0].segments[0].numberOfStops as number_of_stops",
    "flight_offer.itineraries[0].segments[0].blacklistedInEU as blacklisted_in_eu",
    "flight_offer.price.total as total_price",
    "flight_offer.price.currency as currency"
)

output_path = "s3://my-bucket/transformed/"  # Cambia este bucket por tu bucket en S3
extracted_df.write.format("parquet").mode("overwrite").save(output_path)

job.commit()


# s3output = glueContext.getSink(
#   path="s3://my-aws-project-v1/raw/suggestions_info/amadeus/",
#   connection_type="s3",
#   updateBehavior="UPDATE_IN_DATABASE",
#   partitionKeys=[],
#   compression="snappy",
#   enableUpdateCatalog=True,
#   transformation_ctx="s3output",
# )
# s3output.setCatalogInfo(
#   catalogDatabase="raw-amadeus-db", catalogTableName="amadeus"
# )
# s3output.setFormat("glueparquet")
# s3output.writeFrame(dyf)
