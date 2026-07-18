from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import logging

import os
from dotenv import load_dotenv
load_dotenv()

def envoyer_rapport():
    # Connexion à la base de données PostgreSQL
    url = URL.create(
        drivername = "postgresql+psycopg2",
        username="airbyte_bovice_pg",
        password=os.environ.get("DB_PASSWORD"),
        host="localhost",
        port=5432,
        database="airbyte_destination_pharm"
    )
    engine = create_engine(url)
    df = pd.read_sql("SELECT * FROM mart.fct_ventes", engine)
    ca_total = df['montant_total'].sum()
    logging.info(f"Le chiffre d'affaire total est : {ca_total}")
    df.to_csv("rapport_ventes.csv", index=False)
    logging.info("Le rapport des ventes a été exporté vers le fichier rapport_ventes.csv")