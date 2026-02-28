from pyspark.sql import SparkSession
from src.transformation import transform

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("/Volumes/my_catalog/source/folder_managed_files/people_basic_csv/", header=True, inferSchema=True)

final_df = transform(df)

final_df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.devops_table")