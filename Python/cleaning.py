import pandas as pd

data = [
    {"nom": "Paracetamol", "stock": 150, "prix": 1000},
    {"nom": "Ibuprofen",   "stock": None, "prix": 1500},  # valeur nulle
    {"nom": "Paracetamol", "stock": 150,  "prix": 1000},  # doublon
    {"nom": "Amoxicillin", "stock": 200,  "prix": None},  # valeur nulle
]

df  = pd.DataFrame(data)

# Detecter les valeurs nulles
#print(df.isnull().sum())

# Remplacer les nulls par 0
#df["stock"] = df["stock"].fillna(0)
#df["prix"] = df["prix"].fillna(0)

#print(df.isnull().sum())

print(df[df.duplicated(keep=False)])