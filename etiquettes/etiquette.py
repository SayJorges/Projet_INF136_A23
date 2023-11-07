import cv2
import numpy as np
from constantes import *
from images.image import *

def decouper(image_etiquette):

    # Liste pour stocker les images des étiquettes
    images_etiquettes = []

    # Liste des caractères de référence de '0' à '9' et de 'a' à 'z'
    caracteres = [str(i) for i in range(10)] + [chr(ord('a') + i) for i in range(26)]

    for caractere in caracteres:
        image = charger_jpeg(CHEMIN_REFERENCES + "\\" + caractere + ".jpg")
        # Découper l'image en 13 morceaux de 40x40
        morceaux = [image[:, i:i + 40] for i in range(0, image.shape[1], 40)]
        images_etiquettes.extend(morceaux)

    images_array = np.array(images_etiquettes)

    return images_array


