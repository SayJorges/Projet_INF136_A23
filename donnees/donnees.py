from constantes import *


def charger_references():
    lettre = REFERENCE_LETTRES
    chiffre = REFERENCE_CHIFFRES
    # cree le dictionnaire
    dictionnaire_caractere = {}
    for nombre in chiffre:
        dictionnaire_caractere.append(nombre)
    for element in lettre:
        dictionnaire_caractere.append(element)

    return dictionnaire_caractere


def charger_centroides_reference(*args):
    """
    TODO: À être implémenté par les étudiants.
    """
    raise NotImplementedError("Cette fonction n'est pas implémentée")
