#Imports
from pyspark.sql.functions import *

#configuraions
spark.conf.set(
  "fs.azure.account.key.<storage_account>.dfs.core.windows.net",
  "<Storage_Account_Access_Key>"
)


gold_path = "abfss://ecommerce@ecommercestoragejk.dfs.core.windows.net/gold"

silver_path = "abfss://ecommerce@ecommercestoragejk.dfs.core.windows.net/silver"

#Read from silver
df_silver=(
    spark.readStream
    .format("delta")
    .load(silver_path)
)
#Aggregation: Total sales and total items sold per state per minute
df_gold=(
    df_silver
    .withWatermark("timestamp","1 minute")
    .groupby(
        window("timestamp","1 minute"),
        "state"
    )
    .agg(
        sum("total_amount").alias("total_sales"),
        sum("quantity").alias("total_items")
    )
    .select(
        col("window.start").alias("window_start"),
        col("window.end").alias("window_end"),
        "state",
        "total_sales",
        "total_items"
    )
)

# Write to gold layer
(
    df_gold.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation",gold_path+"/_checkpoint")
    .start(gold_path)
)


