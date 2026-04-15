from pyspark.sql import DataFrame

def add_ingestion_timestamp(df: DataFrame):
    from pyspark.sql.functions import current_timestamp
    return df.withColumn("ingestion_ts", current_timestamp())
