from pyspark.sql.functions import *

data = [
    (1, "Alice", 29),
    (2, "Bob", 35),
    (3, "Cathy", 23)
]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
display(df)