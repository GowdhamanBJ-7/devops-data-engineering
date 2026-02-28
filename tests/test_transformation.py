import pytest
from pyspark.sql import SparkSession
from src.transformation import transform

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("test").getOrCreate()

def test_transform(spark):
    data = [(1, 100), (2, None), (1, 100)]
    df = spark.createDataFrame(data, ["id", "amount"])
    
    result = transform(df)
    
    assert result.count() == 1
    assert "amount_with_tax" in result.columns