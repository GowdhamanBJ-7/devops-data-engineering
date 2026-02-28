from pyspark.sql import functions as F

silver_df = spark.table("workspace.default.sales_silver")

gold_df = (
    silver_df
    .groupBy("customer_id")
    .agg(F.sum("amount").alias("total_amount"))
)

gold_df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.sales_gold")