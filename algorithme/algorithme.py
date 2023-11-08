from images.image import *
from donnees.donnees import *
from constantes import *
from etiquettes.etiquette import *


def identifier_caracteres_avec_distances(image_a_identifier, base_de_donnees):
    # Vérifier que l'image reçue a la taille attendue
    if image_a_identifier.shape != (40, 40):
        raise ValueError("La taille de l'image reçue ne correspond pas à la taille attendue (40x40).")

    caractere_identifie = None
    distance_minimale = float('inf')

    for caractere_reference, image_reference in base_de_donnees.items():
        # Calculer la distance entre l'image à identifier et l'image de référence
        distance = calculer_difference(image_a_identifier, image_reference)

        if distance < distance_minimale:
            distance_minimale = distance
            caractere_identifie = caractere_reference

    return caractere_identifie


def lire_etiquette_distances(image_etiquette, base_de_donnees):
    tableau = decouper(image_etiquette)  # retourne des images en tableau découpé de l'étiquette [a,s,s,y]

    code = str()

    for i in range(0, 13, 1):  # essaye de parcourir le tableau
        code += (identifier_caracteres_avec_distances(tableau[i], base_de_donnees))

    return code
