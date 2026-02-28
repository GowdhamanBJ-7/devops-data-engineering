from pyspark.sql import SparkSession
from src.transformation import transform

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("/Volumes/customer_order_details/customer/customer_volume/20240105_sales_customer.csv", header=True, inferSchema=True)

final_df = transform(df)

final_df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.devops_table")