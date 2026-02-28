from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv(
    "/Volumes/customer_order_details/customer/customer_volume/20240105_sales_customer.csv",
    header=True,
    inferSchema=True
)

df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.sales_bronze")