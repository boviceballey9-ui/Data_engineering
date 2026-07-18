import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername = "postgresql+psycopg2",
    username   = "airbyte_bovice_pg",
    password   = os.environ.get("DB_PASSWORD"),
    host       = "localhost",
    port       = 5432,
    database   = "airbyte_destination_pharm"
)

engine  = create_engine(url)

df = pd.DataFrame([
    {"nom" : "Paracetamol", "stock" : "150", "prix" : "1000"},
    {"nom" : "Ibuprofen", "stock" : "80", "prix" : "1500"}
])

#Exporter vers csv
df.to_csv("export_medicaments.csv", index=False)

#Exporter vers Excel
df.to_excel("export_medicaments.xlsx", index=False)

#Exporter vers postgresql
df.to_sql(
    name = "rapport_medicaments", # nom de la table
    con = engine,
    schema = "public",
    if_exists = "replace",
    index = False
)

print("Export fini")