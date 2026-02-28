from pyspark.sql import functions as F

bronze_df = spark.table("workspace.default.sales_bronze")

silver_df = (
    bronze_df
    .dropDuplicates()
    .filter(F.col("amount").isNotNull())
)

silver_df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.sales_silver")