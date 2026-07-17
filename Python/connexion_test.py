import psycopg2

with psycopg2.connect(
    host      = "localhost",
    port      = 5432,
    dbname      = "airbyte_destination_pharm",
    user      = "airbyte_bovice_pg",
    password  = "Ravis@2001"
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT *FROM mart.dim_medicament LIMIT 5")
        resultats = cursor.fetchall()
        for row in resultats:
            print(row)