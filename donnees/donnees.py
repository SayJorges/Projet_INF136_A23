from constantes import *
from references import *
from images.image import *


def charger_references():
    lettre = REFERENCE_LETTRES
    chiffre = REFERENCE_CHIFFRES

    # cree le dictionnaire
    dictionnaire_caractere = {}

    # charger une image
    charger_jpeg()
    for nombre in chiffre:
        dictionnaire_caractere[nombre] = [charger_jpeg]

    for element in lettre:
        dictionnaire_caractere[element] = [charger_jpeg]

    return dictionnaire_caractere


def charger_centroides_reference(*args):
    """
    TODO: À être implémenté par les étudiants.
    """
    raise NotImplementedError("Cette fonction n'est pas implémentée")
