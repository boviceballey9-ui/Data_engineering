import pandas as pd
# DataFrame 1 — médicaments
medicaments = pd.DataFrame([
    {"id_med": 1, "nom": "Paracetamol"},
    {"id_med": 2, "nom": "Ibuprofen"},
    {"id_med": 3, "nom": "Amoxicillin"},
])

# DataFrame 2 — ventes
ventes = pd.DataFrame([
    {"id_med": 1, "montant": 3000},
    {"id_med": 2, "montant": 1500},
    {"id_med": 1, "montant": 2000},
])

df_merge = medicaments.merge(ventes, on="id_med", how="left")

print(df_merge)
