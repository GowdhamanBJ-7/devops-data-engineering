from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = (
    spark.read
    .format("csv")
    .option("header", True)
    .load("/Volumes/my_catalog/source/folder_managed_files/people_basic_csv/")
)

df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.sales_bronze")