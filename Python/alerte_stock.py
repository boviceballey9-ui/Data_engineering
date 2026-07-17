import pandas as pd
import logging
import argparse
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

## Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def verifier_stock(seuil: int = 50):
    # Connexion à la base de données PostgreSQL
    url = URL.create(
        drivername = "postgresql+psycopg2",
        username   = "airbyte_bovice_pg",
        password   = "Ravis@2001",
        host       = "localhost",
        port       = 5432,
        database   = "airbyte_destination_pharm"
    )
    engine = create_engine(url)
    logging.info("Connexion à la base de données réussie.") 

    # Récupération des données de la table fct_achats
    query = "SELECT * FROM mart.fct_achats"
    df = pd.read_sql(query, engine)

    #verification du stock
    for index, row in df.iterrows():
        if row["quantite"]< seuil:
            logging.warning(f"Le stock du medicament {row['id_medicament']} est inférieur au seuil de {seuil}. Quantité actuelle : {row['quantite']}")

    logging.info("Vérification du stock terminée.")


# __main__ est le nom que Python donne automatiquement au fichier que tu exécutes directement.
if __name__ == "__main__":
    # Crée un outil qui lit les arguments passés dans PowerShell. → "Je prépare un lecteur d'arguments"
    parser = argparse.ArgumentParser()
    parser.add_argument("--seuil", type=int, default=50)

    #Lit ce que tu as tapé dans PowerShell :
    args = parser.parse_args()

    #Appelle la fonction avec la valeur récupérée :
    verifier_stock(seuil=args.seuil)