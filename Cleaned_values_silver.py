#Imports
from pyspark.sql.functions import *

#configuraions
spark.conf.set(
  "fs.azure.account.key.<storage_account>.dfs.core.windows.net",
  "<Storage_Account_Access_Key>"
)

bronze_path = "abfss://ecommerce@ecommercestoragejk.dfs.core.windows.net/bronze"

silver_path = "abfss://ecommerce@ecommercestoragejk.dfs.core.windows.net/silver"

#Reading raw data from bronze
df_bronze=(
  spark.readStream
  .format("delta")
  .load(bronze_path)
)

#Clean and enrich
df_clean=(
  df_bronze
  .withColumn("timestamp",to_timestamp("timestamp"))
  .withColumn("price",when(col("price").isNull(),0.0).otherwise(col("price")))
  .withColumn("quantity",when(col("quantity").isNull(),1).otherwise(col("quantity")))
  .withColumn("total_amount",col("price")*col("quantity"))
  .dropDuplicates(["order_id"])
  .filter(col("country")=="USA")
  .filter(col("state").isNotNull())
)
#Write to Silver Layer
(
  df_clean.writeStream
 .format("delta")
 .outputMode("append")
 .option("checkpointLocation",silver_path+"/_checkpoint")
 .start(silver_path)
 )




