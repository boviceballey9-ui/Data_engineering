import psycopg2
import os

with psycopg2.connect(
    host = "localhost",
    port = 5432,
    dbname = "airbyte_destination_pharm",
    user = "airbyte_bovice_pg",
    password = os.environ.get("DB_PASSWORD")
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT SUM(montant_total) AS CA FROM mart.fct_ventes")
        res = cursor.fetchone()
        ca = res[0] if res[0] is not None else 0
        print(f"Le chiffre d'affaire est : {ca}")
