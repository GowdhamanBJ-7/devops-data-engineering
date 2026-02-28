from pyspark.sql import functions as F

def clean_data(df):
    df = df.dropDuplicates()
    df = df.filter(F.col("amount").isNotNull())
    return df

def enrich_data(df):
    df = df.withColumn("amount_with_tax", F.col("amount") * 1.18)
    return df

def transform(df):
    df = clean_data(df)
    df = enrich_data(df)
    return df