import cv2

from constantes import *

from images.image import *


def charger_references():
    # cree le dictionnaire
    dictionnaire_caractere = {}

    # charger une image
    for element in REFERENCE_LETTRES_CHIFFRES:
        image = charger_jpeg(CHEMIN_REFERENCES + "\\" + element + ".jpg")

        dictionnaire_caractere[element] = image

    return dictionnaire_caractere


def charger_etiquettes():
    # Chemin vers le répertoire contenant les étiquettes
    repertoire_etiquettes = CHEMIN_RACINE + '\\donnees\\etiquettes'

    # Liste pour stocker les images des étiquettes
    images_etiquettes = []

    # Liste des caractères de référence de '0' à '9' et de 'a' à 'z'
    #caracteres = charger_references()
    # Liste des caractères de référence de '0' à '9' et de 'a' à 'z'
    caracteres = [str(i) for i in range(10)] + [chr(ord('a') + i) for i in range(26)]

    for caractere in caracteres:
        image = charger_jpeg(CHEMIN_REFERENCES + "\\" + caractere + ".jpg")
        # Découper l'image en 13 morceaux de 40x40
        for i in range(0, image.shape[1], 40):
            morceau = image[:, i:i + 40]
            images_etiquettes.append(morceau)

    return images_etiquettes


def charger_centroides_reference(*args):
    """
    TODO: À être implémenté par les étudiants.
    """
    raise NotImplementedError("Cette fonction n'est pas implémentée")
