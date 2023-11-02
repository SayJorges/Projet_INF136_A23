import cv2

from constantes import *

from images.image import *


def charger_references():
    # Crée le dictionnaire
    dictionnaire_caractere = {}

    # Charger une image
    for element in REFERENCE_LETTRES_CHIFFRES:
        image = charger_jpeg(CHEMIN_REFERENCES + "\\" + element + ".jpg")

        dictionnaire_caractere[element] = image

    return dictionnaire_caractere

def charger_etiquettes():
    # Charger l'image de l'étiquette
    image_etiquette = charger_references()

    if image_etiquette is None:
        raise FileNotFoundError("Impossible de charger l'image de l'étiquette.")

    # Assurez-vous que l'image de l'étiquette a les dimensions attendues (40x520)
    if image_etiquette.shape != (40, 520):
        raise ValueError("L'image de l'étiquette ne correspond pas à la taille attendue (40x520).")

    # Initialiser une liste pour stocker les 13 caractères
    etiquettes = []

    # Découper l'image de l'étiquette en 13 images 40x40
    for i in range(len(etiquettes)):
        debut_colonne = i * 40
        fin_colonne = debut_colonne + 40
        caractere = image_etiquette[:, debut_colonne:fin_colonne]
        etiquettes.append(caractere)

    return etiquettes


def charger_centroides_reference(*args):
    """
    TODO: À être implémenté par les étudiants.
    """
    raise NotImplementedError("Cette fonction n'est pas implémentée")
