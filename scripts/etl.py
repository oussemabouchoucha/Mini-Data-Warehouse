from pyspark.sql import SparkSession

# Créer une session Spark
spark = SparkSession.builder \
    .appName("Mini Data Warehouse") \
    .config("spark.master", "local") \
    .getOrCreate()

# Lecture des fichiers CSV
sales_df = spark.read.option("header", True).csv("data/raw/sales.csv")
customers_df = spark.read.option("header", True).csv("data/raw/customers.csv")

# Sauvegarder les fichiers dans la couche Bronze
sales_df.write.mode("overwrite").parquet("output/bronze/sales")
customers_df.write.mode("overwrite").parquet("output/bronze/customers")

# Nettoyage des données pour la couche Silver
sales_clean_df = sales_df.select("SaleID0", "CustomerID", "ProductID", "Quantity", "UnitPrice", "Discount")
customers_clean_df = customers_df.select("CustomerID", "ContactName", "Phone")

# Sauvegarder les données nettoyées dans la couche Silver
sales_clean_df.write.mode("overwrite").parquet("output/silver/sales_clean")
customers_clean_df.write.mode("overwrite").parquet("output/silver/customers_clean")

# Jointure des ventes et des clients
enriched_df = sales_clean_df.join(customers_clean_df, "CustomerID")

# Sauvegarder la table enrichie dans la couche Gold
enriched_df.write.mode("overwrite").parquet("output/gold/enriched_sales")

# Créer une vue temporaire pour interroger les données
enriched_df.createOrReplaceTempView("enriched_sales")

# Requête SQL pour calculer le revenu total par produit
result = spark.sql(""" 
    SELECT ProductID, SUM(Quantity * (UnitPrice*(1-Discount))) AS TotalRevenue 
    FROM enriched_sales 
    GROUP BY ProductID 
""")
result.show()

# Configuration JDBC pour SQL Server
jdbc_url = "jdbc:sqlserver://OUSSEMA;databaseName=Sales_first_try;integratedSecurity=true;encrypt=true;trustServerCertificate=true"

jdbc_properties = {
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# Exporter la table enrichie vers SQL Server
enriched_df.write.jdbc(url=jdbc_url, table="enriched_sales", mode="overwrite", properties=jdbc_properties)



# jdbc_url = "jdbc:sqlserver://DESKTOP-D9JCVO4;databaseName=MiniDataWarehouse;integratedSecurity=true"

# jdbc_properties = {
#     "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
# }
