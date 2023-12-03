# Librairies générales
import numpy as np
import os
import math
# Librairies images
import matplotlib.pyplot as plt

# Constantes internes
from constantes import RGB_MAX


# from donnees.donnees import *


def charger_jpeg(chemin: str) -> np.ndarray:
    """
    Charge une image donnée en format JPEG et la retourne sous la forme d'un tableau NumPy.

    Arguments:
        chemin (str): Le chemin menant vers l'image à charger.

    Retourne:
        (np.ndarray): L'image chargée.

    TODO: Cette fonction est fournie.
    """

    # Valider que l'image existe
    if not os.path.exists(chemin):
        raise FileExistsError(f"Le fichier n'existe pas : {chemin}")

    # Valider qu'il s'agit d'une image en format JPEG
    if not chemin.endswith('.jpg'):
        raise TypeError(f'Seules les images en format JPEG sont supportées')

    # Charger l'image avec la librairie Matplotlib
    image = plt.imread(chemin) / RGB_MAX

    # Valider le chargement
    if image is None:
        raise IOError("Échec lors de l'ouverture de l'image")

    return image


def afficher(image: np.ndarray, titre: str = '', bloquer: bool = True) -> None:
    """
    Affiche une image donnée sous forme de tableau NumPy.

    Arguments:
        image (np.ndarray): L'image à afficher.
        titre (str): Titre de la figure.
        bloquer(bool) : Détermine si l'on bloque sur la figure ou non.

    Retourne:
        Rien.

    TODO: À être modifié par les étudiants.
    """

    # Créer l'image
    if not bloquer:
        plt.figure()

    plt.imshow(image, cmap='gray')

    # Ajout d'une grille
    plt.grid(True, color='white', linestyle='--', alpha=0.5)

    # Nommer les axes
    plt.xlabel('Largeur')
    plt.ylabel('Hauteur')

    # Ajouter le titre
    plt.title(titre)

    # Afficher l'image
    if not bloquer:
        plt.show(block=False)
        plt.pause(.001)

    else:
        plt.show()


def appliquer_rotation(image: np.ndarray, angle_degres: float) -> np.ndarray:
    """
    Applique une rotation à une image.

    Note: Ceci est une implémentation manuelle.

    Args:
        image (np.ndarray): L'image à tourner.
        angle_degres (float): L'angle de rotation en degrés.

    Retourne:
        (np.ndarray): L'image tournée.

    TODO: Cette fonction est fournie.
    """

    # Trouver le centre de l'image
    xc, yc = image.shape[1] // 2, image.shape[0] // 2

    # Transformer l'angle en radians
    angle_radians = np.radians(angle_degres)

    # Les valeurs trigonométriques de l'angle
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)

    # Extraire les dimensions de l'image
    hauteur, largeur = image.shape

    # Initialiser l'image tournée
    image_tournee = np.zeros((hauteur, largeur)) * RGB_MAX

    # Appliquer la rotation
    for y in range(hauteur):
        for x in range(largeur):

            # Calculer les nouvelles coordonnées du pixel courant
            x_ = (x - xc) * cos_theta - (y - yc) * sin_theta + xc
            y_ = (x - xc) * sin_theta + (y - yc) * cos_theta + yc

            # Trouver le pixel le plus près
            x_voisin = int(x_)
            y_voisin = int(y_)

            # Copier la couleur d'un voisin immédiat pour éviter les inclusions
            if 0 <= x_voisin < largeur and 0 <= y_voisin < hauteur:
                image_tournee[y, x] = image[y_voisin, x_voisin]

    return image_tournee






def calculer_centroide(image):

    """
    Description : Calcule le centroïde d’une image.

    Arguments :
        L’image de référence.

    Retourne : Les coordonnées 𝑥 𝑐 𝑦 𝑐 du centroïde.

    """

    x_c, y_c = 0, 0

    # Initialiser la somme des valeurs de l'image
    somme_valeurs = 0

    # Obtenir les dimensions de l'image
    largeur = len(image[0])
    hauteur = len(image)

    # Parcourir les pixels de l'image
    for y in range(hauteur):
        for x in range(largeur):
            pixel = image[y][x]
            somme_valeurs += (pixel)
            x_c += x * pixel
            y_c += y * pixel

    # Gérer les divisions par zéro
    if somme_valeurs == 0:
        x_c, y_c = 0, 0
    else:
        x_c /= somme_valeurs
        y_c /= somme_valeurs

    return (x_c, y_c)


def calculer_difference(image, image_2):

    """
    Description : Calcule la somme des distances absolues entre chacun des pixels correspondants de deux images.

    Arguments :
        La première image.
        La deuxième image.

    Retourne : La distance entre les deux images.

    """
    distance = 0
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            distance += (abs(image[i, j] - image_2[i, j]))

    return distance


def calculer_moments_premier_ordre(image):
    # Obtenez les dimensions de l'image (largeur et hauteur)
    largeur = len(image)
    hauteur = len(image[0])

    # Initialisez les variables pour les moments du premier ordre en 𝑥, 𝑦 et la masse
    moment_x = 0
    moment_y = 0
    masse = 0

    # Parcourez les pixels de l'image avec des boucles for imbriquées
    for i in range(hauteur):
        for j in range(largeur):
            # Obtenez la valeur du pixel à la position (i, j)
            pixel_value = image[i, j]

            # Mettez à jour les moments du premier ordre en 𝑥, 𝑦 et la masse
            moment_x += pixel_value * j
            moment_y += pixel_value * i
            masse += pixel_value

    return moment_x, moment_y, masse


def calculer_moments_deuxieme_ordre(image):

    """
    Description : Calcule les moments du premier ordre d’une image.

    Arguments :
        L’image de référence.

    Retourne : Le moment en 𝑥 (c.-à-d. la coordonnée 𝑗 du tableau-image). Le moment en 𝑦 (c.-à-d. la coordonnée 𝑖 du
        tableau-image). La « masse » de l’image.
    """
    # Récupérer les dimensions de l'image

    # Initialiser les moments du deuxième ordre
    mu_xy = 0
    mu_xx = 0
    mu_yy = 0
    xc, yc = calculer_centroide(image)
    # Calculer les moments du deuxième ordre en utilisant les équations 4, 5 et 6
    for i in range(len(image)):
        for j in range(len(image[0])):
            pixel_value = image[i, j]

            mu_xy += pixel_value * (j - xc) * (i - yc)
            mu_xx += pixel_value * (j - xc) ** 2
            mu_yy += pixel_value * (i - yc) ** 2

    return mu_xy, mu_xx, mu_yy


def calculer_matrice_covariance(image):

    """
    Description : Calcule la matrice de covariance d’une image.

    Arguments :
        Une image.

    Retourne : Un tableau2D numpy représentant la matrice de covariance.
    """
    # Calculer les moments du deuxième ordre
    mu_xy, mu_xx, mu_yy = calculer_moments_deuxieme_ordre(image)

    # Calculer la matrice de covariance en utilisant l'équation 7
    covariance_matrix = np.array([[mu_xx, mu_xy],
                                  [mu_xy, mu_yy]])

    return covariance_matrix


def calculer_vecteurs_propres(image):

    """
    Description : Calcule les vecteurs propres d’une image.

    Arguments :
        Une image.

    Retourne : Un tableau 1d numpy représentant le premier vecteur propre. Un tableau 1d numpy représentant le premier vecteur propre.
    """
    # Assumez que l'image est une matrice 2x2, comme indiqué dans l'énoncé
    # Vous devrez adapter cela en fonction du format réel de vos images

    vec1,vec2 = calculer_matrice_covariance(image)

    mu_xx = vec1[0]
    mu_yy = vec2[1]
    mu_xy = vec1[1]


    # Calcul des coefficients de l'équation quadratique
    a = 1
    b = -(mu_xx + mu_yy)
    c = mu_xx * mu_yy - mu_xy ** 2

    # Calcul des valeurs propres
    delta = b ** 2 - 4 * a * c

    # Assurez-vous que le discriminant est non négatif pour éviter les erreurs de racine carrée négative
    if delta >= 0:
        lambda1 = (-b + np.sqrt(delta)) / (2 * a)
        lambda2 = (-b - np.sqrt(delta)) / (2 * a)

        # Calcul des vecteurs propres
        v1_unnormalized = np.array([mu_xy, lambda1 - mu_xx])
        v2_unnormalized = np.array([mu_xy, lambda2 - mu_xx])

        # Normalisation des vecteurs propres
        v1 = v1_unnormalized / np.linalg.norm(v1_unnormalized)
        v2 = v2_unnormalized / np.linalg.norm(v2_unnormalized)

        # Retourner les vecteurs propres en ordre décroissant de valeurs propres
        if lambda1 > lambda2:
            return [v1, v2]
        else:
            return [v2, v1]
    else:
        # Si le discriminant est négatif, renvoyer une valeur indicative (par exemple, None)
        return None
import numpy as np

def estimer_angle_rotation(image):
    """
    Estime l'angle de rotation d'une image.

    Arguments :
    - image : Une image représentée par une matrice.

    Retourne :
    - L'angle estimé en degrés.
    """

    # Calculer les vecteurs propres
    v_propres = calculer_vecteurs_propres(image)

    if v_propres is not None:
        # Récupérer les composantes des vecteurs propres

        v1x,v2x= v_propres[0][0],v_propres[1][0]

        # Calculer l'angle en radians en utilisant l'Equation 11
        angle_radians = (math.pi/2) -abs(math.atan2(v2x,v1x))

        # Convertir l'angle en radians en degrés
        angle_degrees = angle_radians * (180/math.pi)

        return angle_degrees
    else:
        # Gérer le cas où les vecteurs propres ne peuvent pas être calculés
        return None


