from pyspark.sql import functions as F

bronze_df = spark.table("workspace.default.sales_bronze")

silver_df = (
    bronze_df
    .withColumn("last_name", F.trim(F.split(F.col("Name"), ",")[0]))
    .withColumn("first_name", F.trim(F.split(F.col("Name"), ",")[1]))
    .drop("Name")
)

df_silver = silver_df.withColumn(
    "id",
    F.sha2(F.concat_ws("||", F.col("first_name"), F.col("last_name")), 256)
)

df_silver.write.mode("overwrite").option('overwriteschema','true').saveAsTable("workspace.default.sales_silver")