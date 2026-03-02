import pytest
from pyspark.sql import SparkSession

from notebooks.utils.silver import transform_silver
from notebooks.utils.gold import transform_gold

@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.master("local[1]").appName("test").getOrCreate()
    yield spark
    spark.stop()


def test_transform_silver(spark):
    data = [("John, Doe", "25")]
    columns = ["Name", "Age"]
    bronze_df = spark.createDataFrame(data, columns)

    silver_df = transform_silver(bronze_df)
    result = silver_df.collect()

    assert "first_name" in silver_df.columns
    assert "last_name" in silver_df.columns
    assert "id" in silver_df.columns
    assert result[0]["first_name"] == "Doe"

# Assertions - It checks whether the transformation created these new columns.

def test_transform_gold(spark):
    data = [("Doe", "John", "25", "abc")]
    columns = ["last_name", "first_name", "Age", "id"]
    silver_df = spark.createDataFrame(data, columns)

    gold_df = transform_gold(silver_df)
    result = gold_df.collect()

    assert result[0]["age_group"] == "Young"
    assert isinstance(result[0]["Age"], int)