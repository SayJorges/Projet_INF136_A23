
# Librairies générales
import numpy as np
import pickle
import random
import os

# Librairies pour l'affichage
import cv2

# Librairies internes
from images.image import (
    appliquer_rotation,
    estimer_angle_rotation,
    afficher,
)


def exemple_sauvegarde_pickle():
    """
    Exemple de sauvegarde avec la librairie pickle.
    """

    # Message de test à sauvegarder
    message = 'Cornichon'

    # Sauvegarde en mode écriture binaire ('wb')
    with open('test_pickle.pkl', 'wb') as fichier:
        pickle.dump(message, fichier)


def exemple_chargement_pickle():
    """
    Exemple de chargement avec la librairie pickle.
    """

    # Valider
    if not os.path.exists('test_pickle.pkl'):
        FileExistsError('Exécutez exemple_sauvegarde_pickle en premier!')

    # Charger en mode lecture binaire ('rb')
    with open('test_pickle.pkl', 'rb') as fichier:
        message = pickle.load(fichier)

    # Afficher le message chargé
    print(f'Le message lu est : {message}')


def exemple_pickle():
    """
    Exemple complet pour la sauvegarde et le chargement avec la librairie pickle.
    """

    # Sauvegarde un message (str)
    exemple_sauvegarde_pickle()

    # Charge le message à partir de la sauvegarde
    exemple_chargement_pickle()


def main():

    # Définire les dimensions des caractères aléatoires
    hauteur = 150
    largeur = 150

    # Paramètres de la police d'écriture
    police = cv2.QT_FONT_NORMAL
    echelle = 3
    epaisseur = 3
    couleur = (128, 0, 0)

    while True:

        # Le caractère aléatoire à replacer
        texte = chr(random.randint(ord('A'), ord('Z')))

        # Obtenir les dimensions
        taille_texte = cv2.getTextSize(texte, police, echelle, epaisseur)[0]

        # Calculer la position du centre du caractère
        x = (largeur - taille_texte[0]) // 2
        y = (hauteur + taille_texte[1]) // 2

        # Créer un canevas 150 x 150 pixels
        image = np.random.randint(0, 5, (hauteur, largeur))

        # Ajouter le caractère au canevas
        cv2.putText(image, texte, (x, y), police, echelle, couleur, epaisseur)

        # Afficher le caractère brut
        afficher(image, 'Caractère original')

        # Appliquer la rotation aléatoire de +/- [20, 45] degrés
        angle_rotation_degres = (-1) ** random.randint(0, 1) * random.randint(20, 45)
        caractere_tourne = appliquer_rotation(image, angle_rotation_degres)

        # Afficher l'angle réel
        print(f'Angle de rotation: {angle_rotation_degres} degrés')

        # Afficher le caractère tourné
        afficher(caractere_tourne, 'Caractère tourné')

        # Estimer l'angle de rotation
        angle_rotation_approximatif = estimer_angle_rotation(caractere_tourne)

        # Afficher l'angle de rotation estimé
        print(f'Angle de rotation estimé: {angle_rotation_approximatif} degrés')

        # Corriger la rotation
        caractere_corrige = appliquer_rotation(caractere_tourne, -angle_rotation_approximatif)

        # Afficher le caractère repositionné
        afficher(caractere_corrige, 'Caractère repositionné')


if __name__ == '__main__':
    main()
