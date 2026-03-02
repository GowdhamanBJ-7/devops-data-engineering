from pyspark.sql import functions as F

def transform_gold(silver_df):

    gold_df = (
        silver_df
        .withColumn("Age", F.col("Age").cast("int"))
        .withColumn(
            "age_group",
            F.when(F.col("Age") < 30, "Young")
             .otherwise("Senior")
        )
    )

    return gold_df

silver_df = spark.table("workspace.default.sales_silver")

gold_df = transform_gold(silver_df)

gold_df.write.mode("overwrite").saveAsTable("workspace.default.sales_gold")