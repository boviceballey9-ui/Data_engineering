# List
medicaments = ["Paracetamol", "Ibuprofen", "Amoxicillin", "Aspirin", "Metformin"]

#Dict
vente = {
  "id_vente": 1,
  "medicament": "Paracetamol",
  "quantite": 3,
  "prix_unitaire": 12
}

# List of Dict
resultats = [
    {
        "id_vente": 1,
        "nom": "Paracetamol",
        "stock": 150
    },
    {
        "id_vente": 2,
        "nom": "Ibuprofen",
        "stock": 80
    }
]

#loop
for vente in resultats:
    if vente["stock"] < 100:
        print(f"Le stock du medicament {vente['nom']} est faible: {vente['stock']} unités restantes.")
    else:    
    
        print(f"Le stock du medicament {vente['nom']} est suffisant: {vente['stock']} unités restantes.")   