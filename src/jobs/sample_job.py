from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("GlueLocalTest").getOrCreate()

    data = [("Alice", 1), ("Bob", 2)]
    df = spark.createDataFrame(data, ["name", "id"])

    df.show()

    spark.stop()


if __name__ == "__main__":
    main()
