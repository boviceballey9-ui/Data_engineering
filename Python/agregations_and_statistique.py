import pandas as pd

data = [
    {"medicament": "Paracetamol", "quantite": 3, "montant": 3000},
    {"medicament": "Ibuprofen",   "quantite": 1, "montant": 1500},
    {"medicament": "Paracetamol", "quantite": 2, "montant": 2000},
    {"medicament": "Amoxicillin", "quantite": 5, "montant": 10000},
]

df = pd.DataFrame(data)

# GROUP BY medicament → SUM quantite et montant
#En groupant les medicaments, extrait la somme des quantites, la somme des montants et la moyenne des montants
resultat = df.groupby("medicament").agg(
    total_quantite = ("quantite", "sum"),
    total_montant = ("montant", "sum"),
    moyenne_montant = ("montant", "mean")
).reset_index()

print(resultat)