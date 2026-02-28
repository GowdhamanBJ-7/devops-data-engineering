from pyspark.sql import functions as F
from pyspark.sql.window import Window

bronze_df = spark.table("workspace.default.sales_bronze")

silver_df = (
    bronze_df
    .withColumn("last_name", F.trim(F.split(F.col("Name"), ",")[0]))
    .withColumn("first_name", F.trim(F.split(F.col("Name"), ",")[1]))
    .drop("Name")
)
window_spec = Window.orderBy(F.monotonically_increasing_id())

df_silver = silver_df.withColumn("id", F.row_number().over(window_spec))

df_silver.write.mode("overwrite").saveAsTable("workspace.default.sales_silver")