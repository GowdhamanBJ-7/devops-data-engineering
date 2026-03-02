from pyspark.sql import functions as F

silver_df = spark.table("workspace.default.sales_silver")

gold_df = (
    silver_df
    .withColumn("Age", F.col("Age").cast("int"))
    .withColumn(
        "age_group",
        F.when(F.col("Age") < 30, "Young")
         .otherwise("Senior")
    )
)

gold_df.write.mode("overwrite").saveAsTable("workspace.default.sales_gold")