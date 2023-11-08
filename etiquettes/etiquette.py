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
