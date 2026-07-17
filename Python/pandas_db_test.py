import pandas as pd
import psycopg2
import os

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    dbname = "airbyte_destination_pharm",
    user = "airbyte_bovice_pg",
    password = os.environ.get("DB_PASSWORD")
)

df = pd.read_sql("SELECT * FROM mart.fct_ventes", conn)
print(df.head()) 
print(f"Le chiffre d'affaire total est : {df['montant_total'].sum()}")
conn.close()

