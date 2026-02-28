from pyspark.sql import functions as F

silver_df = spark.table("workspace.default.sales_silver")

gold_df = silver_df.withColumn(
    "age_group",
    F.when(F.col("Age") < 30, "Young")
     .otherwise("Senior")
)
df_gold_summary = (
    gold_df
    .groupBy("age_group")
    .agg(
        F.count("*").alias("total_people"),
        F.round(F.avg("Age"), 2).alias("avg_age")
    )
)
df_gold_summary.write.mode("overwrite").saveAsTable("workspace.default.sales_gold")