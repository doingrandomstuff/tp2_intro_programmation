import data
# import module_catalogue
# import module_ventes
from conversion import safe_cast

while True:
    print("1. Ajouter un produit")
    print("2. Afficher le catalogue")
    print("3. Réapprovisionner")
    print("4. Enregistrer une vente")
    print("5. Historique des ventes")
    print("0. Quitter")

    choix = safe_cast(input("Choix : "),int,10)

    if choix == 1:
        pass
    elif choix == 2:
        pass
    elif choix == 3:
        pass
    elif choix == 4:
        pass
    elif choix == 5:
        pass
    elif choix == 0:
        print("Programme terminé")
        #data.sauvegarder()
        break
    else:
        print("Choix invalide.")