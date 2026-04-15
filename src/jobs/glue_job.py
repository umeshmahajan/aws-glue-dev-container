import sys
import yaml
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

# Import utility
sys.path.append('/home/hadoop/workspace/src')
from common.transformations import add_ingestion_timestamp


def load_yaml_config(path: str):
    """Load YAML from local or S3"""
    if path.startswith("s3://"):
        import boto3
        s3 = boto3.client("s3")
        bucket = path.split("/")[2]
        key = "/".join(path.split("/")[3:])
        obj = s3.get_object(Bucket=bucket, Key=key)
        return yaml.safe_load(obj["Body"].read())
    else:
        with open(path, "r") as f:
            return yaml.safe_load(f)


def load_sql(path: str):
    with open(path, "r") as f:
        return f.read()


def main():
    # ----------------------------
    # 1. Read Job Arguments
    # ----------------------------
    args = getResolvedOptions(sys.argv, [
        'JOB_NAME',
        'ENV',
        'CONFIG_PATH',
        'SQL_PATH'
    ])

    env = args['ENV']
    config_path = args['CONFIG_PATH']
    sql_path = args['SQL_PATH']

    # ----------------------------
    # 2. Initialize Glue Context
    # ----------------------------
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark: SparkSession = glueContext.spark_session

    # ----------------------------
    # 3. Load Config
    # ----------------------------
    config = load_yaml_config(config_path)
    env_config = config[env]

    source_conf = env_config['source']
    dest_conf = env_config['destination']

    # ----------------------------
    # 4. Read Source Data
    # ----------------------------
    df = spark.read.format(source_conf['format']) \
        .options(**source_conf.get('options', {})) \
        .load(source_conf['path'])

    df.createOrReplaceTempView("source_table")

    # ----------------------------
    # 5. Apply SQL Transformation
    # ----------------------------
    sql_query = load_sql(sql_path)
    transformed_df = spark.sql(sql_query)

    # ----------------------------
    # 6. Apply Utility Transformation
    # ----------------------------
    transformed_df = add_ingestion_timestamp(transformed_df)

    # ----------------------------
    # 7. Write to Destination S3
    # ----------------------------
    transformed_df.write \
        .mode(dest_conf.get('mode', 'overwrite')) \
        .format(dest_conf['format']) \
        .save(dest_conf['path'])

    # ----------------------------
    # 8. Optional: Register Table
    # ----------------------------
    if 'table' in env_config:
        table_conf = env_config['table']

        transformed_df.write \
            .mode("overwrite") \
            .format("parquet") \
            .saveAsTable(f"{table_conf['database']}.{table_conf['name']}")

    print("Job completed successfully!")


if __name__ == "__main__":
    main()
