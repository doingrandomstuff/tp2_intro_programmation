import json

filename = "data.json"


# sauvegarder un dictionnaire "d"
def sauvegarder(d):
    if type(d) != type({}):
        raise TypeError("d doit être un dictionnaire")

    with open(filename, "w") as file:
        json.dump(d, file) # écriture dans fichier data.json

    print("Sauvegarde réussie")


 # lire le fichier et charger les données (d = charger())
def charger():
    d = {}  

    try:
        with open(filename, "r") as file:
            d = json.load(file)

    except json.JSONDecodeError: # fichier invalide/vide
        print("Aucune sauvegarde valide trouvée.")
        d = init_structure_vide()

    return d


# créer la structure vide si ya aucune données existantes
def init_structure_vide():
    return {"produits":[], "quantite": []}


# créer un dictionnaire pour un nouveau produit (classes are better tho)
def creer_produit(id, nom, prix_unitaire, quantite):
    return {"id": id, "nom": nom, "prix_unitaire": prix_unitaire, "quantite": quantite}