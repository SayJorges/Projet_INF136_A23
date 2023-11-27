# Librairies générales
import numpy as np
import pytest

# Librairies testées
from images.image import *


def test_calculer_difference():
    # Test d'une différence nulle en comparant une image à elle-même.
    image = np.random.randint(0, 10, (5, 5))
    #
    assert calculer_difference(image, image) == 0
    #
    #    #
    #    #Test d'une différence positive en comparant une image avec des pixels allumés à une image vide.
    #    # La probabilité d'un faux positif est égale à (1/10)^25.
    #    #
    #
    image = np.random.randint(0, 10, (5, 5))
    image_vide = np.zeros((5, 5))
    #
    assert calculer_difference(image, image_vide) > 0
    #
    #
    #    #
    #    #Test d'une différence négative en comparant une image avec des pixels allumés à une image vide. Puisque la distance
    #    #est sensée être retourne en valeur absolue, nous nous attendons à une valeur positive.
    #    #
    #    #La probabilité d'un faux positif est égale à (1/10)^25.
    #    #
    #
    image = np.random.randint(0, 10, (5, 5))
    image_vide = np.zeros((5, 5))
    #
    assert calculer_difference(image_vide, image) > 0


#
#
def test_calculer_moments_premier_ordre():
    """
#    Test pour le calcul des moments du premier ordre d'une image.
#
    Moment en x = 1 * 0 + 2 * 1 + 3 * 0 + 4 * 1 = 6
    Moment en y = 1 * 0 + 2 * 0 + 3 * 1 + 4 * 1 = 7
    masse = 1 + 2 + 3 + 4 = 10
    """


# Image de test
image = np.array([[1, 2], [3, 4]])
# Calculer les moments du premier ordre
moment_x, moment_y, masse = calculer_moments_premier_ordre(image)

# Résultats attendus
moment_x_attendu = 6
moment_y_attendu = 7
masse_attendue = 10

assert moment_x == moment_x_attendu and \
       moment_y == moment_y_attendu and \
       masse == masse_attendue


def test_calculer_centroide_image_vide():
    """
   Test avec une image vide dont le centroïde devrait être situé à (0,0).
   """

    # L'image de test
    image = np.zeros((2, 2))

    assert calculer_centroide(image) == (0.0, 0.0)


def test_calculer_centroide_entiers():
    """
   Test avec un seul pixel au centre (1,1) d'une image 3 x 3.
   """

    # Image de test
    image = np.array([[1, 2], [3, 4]])

    assert calculer_centroide(image) == (0.6, 0.7)


def test_calculer_centroide_rationnels():
    """
   Test avec une image dont le centroïde n'atterrit pas sur des coordonnées entières.
   """

    # Image de test
    image = np.array([[0.5, 0], [0, 0.5]])

    assert calculer_centroide(image) == (0.5, 0.5)


def test_calculer_moments_deuxieme_ordre():
    # """
    #    Test pour le calcul des moments du deuxième ordre d'une image.
    #    """

    # Image de test
    image = np.array([[1.25, 20.5], [30.1, 40.5]])

    # Valeurs attendues
    moments_attendus = (-6.13345966432052, 20.707634001082837, 16.627504060638874)

    # Valeurs obtenues
    moments_obtenus = calculer_moments_deuxieme_ordre(image)
    #
    assert np.allclose(moments_obtenus, moments_attendus)


#
#
def test_calculer_matrice_covariance():
    """
   Test pour le calcul de la matrice de covariance.
   """

    # Image de test
    image = np.array([[1.25, 20.5], [30.1, 40.5]])

    # Valeurs attendues
    mu_xy = -6.13345966432052
    mu_xx = 20.707634001082837
    mu_yy = 16.627504060638874

    # La matrice de covariance attendue
    cov_attendue = [[mu_xx, mu_xy], [mu_xy, mu_yy]]

    # La matrice de covariance obtenue
    cov_obtenue = calculer_matrice_covariance(image)

    assert np.allclose(cov_obtenue, cov_attendue)

def test_calculer_vecteurs_propres():
   """
   Test pour le calcul des vecteurs propres.
   """

   # L'image de test
   image = np.array([[0., 1., 0.], [0., 1., 1.], [0., 0., 0.]])

   # Calculer ces vecteurs propres
   v1, v2 = calculer_vecteurs_propres(image)

   # Valeurs attendues
   approx_inv_racine_2 = pytest.approx(1/2 ** 0.5)
   approx_inv_racine_2_negatif = pytest.approx(-1/2 ** 0.5)

   assert v1[0] == approx_inv_racine_2 and \
          v1[1] == approx_inv_racine_2 and \
          v2[0] == approx_inv_racine_2 and \
          v2[1] == approx_inv_racine_2_negatif


# def test_estimer_angle_rotation():
#    """
#    Test pour le calcul des vecteurs propres.
#    """
#
#    # L'image de test
#    image = np.array([[0., 1., 0.], [0., 1., 1.], [1., 0., 0.]])
#
#    # L'angle estimé
#    angle_obtenu = estimer_angle_rotation(image)
#
#    # L'angle attendu
#    angle_attendu = 45.0
#
#    assert abs(angle_obtenu) == abs(angle_attendu)
#
