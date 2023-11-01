from constantes import *
from images.image import *


def charger_references():


    # cree le dictionnaire
    dictionnaire_caractere = {}

    # charger une image
    for elements in REFERENCE_LETTRES_CHIFFRES:

        imagee = charger_jpeg(CHEMIN_REFERENCES + "\\" + elements+ ".jpg")


        dictionnaire_caractere[f"elements.jpg"] = imagee


    return dictionnaire_caractere



def charger_centroides_reference(*args):
    """
    TODO: À être implémenté par les étudiants.
    """
    raise NotImplementedError("Cette fonction n'est pas implémentée")





def charger_etiquettes():

    return list