import pandas as pd

data = [
    {"nom": "Paracetamol", "stock": 150, "prix": 1000},
    {"nom": "Ibuprofen", "stock": 80, "prix": 1500},
    {"nom": "Amoxicillin", "stock": 200, "prix": 2000},
]

df = pd.DataFrame(data)
df2 = pd.DataFrame(data, columns=["nom", "stock"])
df3 = pd.Series(data)
print(df)
#print(df2)
#print(df3)

for i, ligne in df.iterrows():
    print(f"Ligne {i} : {ligne["nom"]} | {ligne["stock"]} | {ligne["prix"]}")