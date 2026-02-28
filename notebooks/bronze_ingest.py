from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("/Volumes/my_catalog/source/folder_managed_files/people_basic_csv/", header=True)


df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.sales_bronze")