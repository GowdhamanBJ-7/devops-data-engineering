from notebooks.utils.silver import transform_silver


bronze_df = spark.table("workspace.default.sales_bronze")
silver_df = transform_silver(bronze_df)

silver_df.write.mode("overwrite").option('overwriteschema','true').saveAsTable("workspace.default.sales_silver")