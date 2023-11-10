import cv2
import numpy as np
from constantes import *
from main import *
from images.image import *
import pickle

def charger_references():
    # cree le dictionnaire
    dictionnaire_caractere = {}

    # charger une image
    for element in REFERENCE_LETTRES_CHIFFRES:
        image = charger_jpeg(CHEMIN_REFERENCES + "\\" + element + ".jpg")

        dictionnaire_caractere[element] = image

    return dictionnaire_caractere


def charger_etiquettes():
    # List to store the images of the labels
    images_etiquettes = []
    REFERENCE_ETIQUETTES = []

    for i in range(1, 41):
        chiffres = str(i)
        REFERENCE_ETIQUETTES.append(chiffres)

    for number in REFERENCE_ETIQUETTES:
        image = charger_jpeg(CHEMIN_ETIQUETTES + "\\" + number + ".jpg")

        # Cut the image into 13 pieces of 40x40
        for j in range(0, image.shape[1], CARACTERE_NB_PIXELS_COTE):
            morceau = image[:, j:j + CARACTERE_NB_PIXELS_COTE]
            images_etiquettes.append(morceau)

    # Stack images horizontally to create a single image
    image_array = np.concatenate(images_etiquettes, axis=1)

    # Separate the image every 520 pixels horizontally and create 40x520 segments
    separated_images = [image_array[:, i:i + 520] for i in range(0, image_array.shape[1], 520)]

    return separated_images


def calculer_centroides_references():
    centroides = {}  # Initialisation du dictionnaire des centroïdes

    # Parcourir chaque symbole de référence
    for image_de_reference in charger_references():
        x_c, y_c = calculer_centroide(image_de_reference)  # Utilisez la fonction pour calculer le centroïde
        centroides[image_de_reference] = (x_c, y_c)  # Stockez les coordonnées du centroïde dans le dictionnaire
        print(f"Symbole : {symbole}, Centroïde : x = {x_c}, y = {y_c}")

    # Créez le répertoire s'il n'existe pas
    os.makedirs('donnees/references/centroides', exist_ok=True)

    # Enregistrez le dictionnaire dans un fichier pickle
    with open('donnees/references/centroides/centroides.pkl', 'wb') as fichier_pickle:
        pickle.dump(centroides, fichier_pickle)


def charger_centroides_reference():
    chemin_fichier_pickle = 'donnees/references/centroides/centroides.pkl'

    if not os.path.exists(chemin_fichier_pickle):
        # Si le fichier pickle n'existe pas, calculez les centroides de références
        calculer_centroides_references()

    # Chargez les centroïdes depuis le fichier pickle
    with open(chemin_fichier_pickle, 'rb') as fichier_pickle:
        centroides = pickle.load(fichier_pickle)

    return centroides
