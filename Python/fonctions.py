def verifier_stock(medicament: dict, seuil: int =100) ->str:
    if medicament['stock'] < seuil:
        return f"ALERTE : {medicament['nom']} sous le seuil"
    return f"OK : {medicament['nom']}"
#print(verifier_stock({"nom": "Paracetamol", "stock": 180}))



def calculer_valeur_stock(medicaments: list): 
    for med in medicaments:
        valeur_stock = med["stock"] * med["prix"]
        print(f" {med['nom']}, {valeur_stock}")

""" calculer_valeur_stock([
    {"nom": "Paracetamol", "stock": 25, "prix": 1000},
    {"nom": "Ibuprofen", "stock": 30, "prix": 1500},
    {"nom": "Amoxicillin", "stock": 20, "prix": 2000}
])  """


    
def rapport_ventes(ventes: list) -> None:
    
    # Étape 1 — Accumulateur
    rapport = {}
    
    for vente in ventes:
        med = vente["medicament"]
        
        # Si le médicament n'existe pas encore dans rapport, on l'initialise
        if med not in rapport:
            rapport[med] = {"quantite": 0, "ca": 0}
        
        # On accumule
        rapport[med]["quantite"] += vente["quantite"]
        rapport[med]["ca"]       += vente["quantite"] * vente["prix_unitaire"]
    
    # Étape 2 — Affichage
    for med, data in rapport.items():
        print(f"{med} → {data['quantite']} unités vendues | Chiffre d'affaires : {data['ca']}")


rapport_ventes([
    {"id_vente": 1, "medicament": "Paracetamol", "quantite": 3, "prix_unitaire": 1000},
    {"id_vente": 2, "medicament": "Ibuprofen",   "quantite": 1, "prix_unitaire": 1500},
    {"id_vente": 3, "medicament": "Amoxicillin", "quantite": 5, "prix_unitaire": 2000},
    {"id_vente": 4, "medicament": "Paracetamol", "quantite": 2, "prix_unitaire": 1000},
])

