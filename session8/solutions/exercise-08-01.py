from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, when


spark = (
    SparkSession.builder
    .appName("Session08Exercise01")
    .master("local[*]")
    .getOrCreate()
)

students = [
    ("Ava", "Data Analytics", 92, 200),
    ("Nikos", "Data Engineering", 28, 30),
    ("Maya", "Data Analytics", 78, 148),
    ("Leo", "Business", 47, 138),
    ("Iris", "Data Engineering", 95, 122),
    ("Elena", "Business", 81, 180),
    ("Omar", "Data Analytics", 58, 198),
    ("Marcos", "Data Engineering", 34, 57),
    ("James", "Business", 60, 69),
    ("Pablo", "Data Analytics", 87, 112),
]

columns = ["name", "track", "score", "hours_studied"]

df = spark.createDataFrame(students, columns)

print("Schema:")
df.printSchema()

print("First 5 rows:")
df.show(5)

print("Scores higher than 85:")
df.filter(df["score"] >= 85).show()

print("DF with results:")
result_df = df.withColumn(
    "result", 
    when(col("score") >= 50, "pass").otherwise("review")
)
result_df.show()

print("Summary group by track:")
df.groupBy("track").agg(count("name").alias("number_of_students"), avg("score").alias("average_score"), avg("hours_studied").alias("average_hours_studied")).show()

spark.stop()
print("End of spark session")