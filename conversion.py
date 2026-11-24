# utils pour input sécuritaire

# convertir valeur s en utilisant une fonction de conversion (int, float, etc)
# si une erreur se produit on retournera valeur_defaut
def safe_cast(s, fonction_conversion, valeur_defaut):
    try:
        return fonction_conversion(s)

    except ValueError:
        return valeur_defaut