
from notebooks.utils.gold import transform_gold

silver_df = spark.table("workspace.default.sales_silver")
gold_df = transform_gold(silver_df)
gold_df.write.mode("overwrite").saveAsTable("workspace.default.sales_gold")