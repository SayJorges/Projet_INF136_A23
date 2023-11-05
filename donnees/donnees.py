import cv2
import numpy as np
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

    # List to store the images of the labels
    images_etiquettes = []

    # List of reference characters from '0' to '9' and 'a' to 'z'
    caracteres = [str(i) for i in range(10)] + [chr(ord('a') + i) for i in range(26)]

    for caractere in caracteres:
        image = charger_jpeg(CHEMIN_REFERENCES + "\\" + caractere + ".jpg")
        # Cut the image into 13 pieces of 40x40
        for i in range(0, image.shape[1], 40):
            morceau = image[:, i:i + 40]
            images_etiquettes.append(morceau)

    # Stack images horizontally to create a single image
    image_array = np.concatenate(images_etiquettes, axis=1)

    # Separate the image every 520 pixels horizontally and create 40x520 segments
    separated_images = [image_array[:, i:i + 520] for i in range(0, image_array.shape[1], 520)]

    return separated_images


def charger_centroides_reference(*args):
    """
    TODO: À être implémenté par les étudiants.
    """
    raise NotImplementedError("Cette fonction n'est pas implémentée")
