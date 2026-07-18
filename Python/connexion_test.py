import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
with psycopg2.connect(
    host      = "localhost",
    port      = 5432,
    dbname      = "airbyte_destination_pharm",
    user      = "airbyte_bovice_pg",
    password  = os.environ.get("DB_PASSWORD")
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT *FROM mart.dim_medicament LIMIT 5")
        resultats = cursor.fetchall()
        for row in resultats:
            print(row)