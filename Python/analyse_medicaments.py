import pandas as pd
import psycopg2
import os

conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    dbname = "airbyte_destination_pharm",
    user = "airbyte_bovice_pg",
    #password = os.environ.get("DB_PASSWORD")
    password = "Ravis@2001"
) 
query = """
SELECT nom_medicament,
    AVG(prix_unitaire) AS pu
FROM mart.dim_medicament AS med
JOIN mart.fct_ventes vte
ON med.id_medicament = vte.id_medicament
GROUP BY nom_medicament
ORDER BY pu DESC
LIMIT 3
"""

query2 = """
SELECT nom_medicament,
    AVG(prix_unitaire) AS pu
FROM mart.dim_medicament AS med
JOIN mart.fct_ventes vte
ON med.id_medicament = vte.id_medicament
GROUP BY med.nom_medicament
"""


query3 = """
SELECT nom_medicament,
    quantite
FROM mart.dim_medicament AS med
JOIN mart.fct_achats ach
ON med.id_medicament = ach.id_medicament
"""
df = pd.read_sql("SELECT * FROM mart.dim_medicament", conn)
df_top3 = pd.read_sql(query, conn)
df_top_3 = pd.read_sql(query2, conn)
df_stock = pd.read_sql(query3, conn)

#Nombre total des lignes dans la table
nbr_ligne = df.shape[0]
#print(f"Le nombre total des medicaments est : {nbr_ligne}")
#print(df_top3)
#print(df_top_3.sort_values("pu", ascending=False).head(3))
print(df_stock[df_stock["quantite"] < 20])

