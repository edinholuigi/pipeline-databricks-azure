# Databricks notebook source
# MAGIC %scala
# MAGIC val util = ("dbutils.fs.")
# MAGIC
# MAGIC

# COMMAND ----------

dbutils.fs.mkdirs("/mnt/dados")

# COMMAND ----------

# MAGIC %python 
# MAGIC dbutils.fs.ls("/mnt")
# MAGIC

# COMMAND ----------

# MAGIC %scala
# MAGIC val configs = Map(
# MAGIC   "fs.azure.account.auth.type" -> "OAuth",
# MAGIC   "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC   "fs.azure.account.oauth2.client.id" -> "90000d82-5353-40eb-a635-1c8a28f4f843",
# MAGIC   "fs.azure.account.oauth2.client.secret" -> "c6q8Q~rO1xZOzUqud.Xg_3HvOCjnDfCeCBmXObeN",
# MAGIC   "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com/2f8c6436-f044-4629-b78f-bf9f807e8f2d/oauth2/token")
# MAGIC // Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC dbutils.fs.mount(
# MAGIC   source = "abfss://imoveis@datalakedinho.dfs.core.windows.net/",
# MAGIC   mountPoint = "/mnt/dados",
# MAGIC   extraConfigs = configs)

# COMMAND ----------

# MAGIC %python 
# MAGIC dbutils.fs.ls("/mnt/dados")

# COMMAND ----------


