import cv2
from donnees.donnees import *
from constantes import *


def decouper(image_etiquette):
    # Lire l'image d'étiquette

    # Assurez-vous que l'image a été chargée avec succès
    # if img is None:
    #     raise ValueError("Impossible de charger l'image d'étiquette.")

    caract = []

    # Extraire chaque caractère sous forme d'image en tableau NumPy
    for image in charger_etiquettes():
        for element in image:
            caract.append(element)
            caract.split(element)

    # # Assurez-vous que nous avons exactement 13 caractères
    if len(caract) != 13:
        raise ValueError("L'image d'étiquette ne contient pas 13 caractères.")

    return caract
import cv2
import numpy as np
from constantes import *
from images.image import *


def decouper(image_etiquette):
    # Liste pour stocker les images des étiquettes
    images_etiquettes = []
    # boucle pour separer en  13 images de 40 caracteres
    for i in range(0, 13, 1):
        images = image_etiquette[0:40, i * 40:(i * 40 + 40)]
        images_etiquettes.append(images)

    return images_etiquettes
