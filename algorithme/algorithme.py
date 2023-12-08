from etiquettes.etiquette import *

def identifier_caracteres_avec_distances(image_a_identifier, base_de_donnees):

    """

        Description : Identifie un caractère alphanumérique par rapport à la distance avec un ensemble de caractères de référence.

        Arguments :
            - image_a_identifier    : L’image du caractère à identifier.
            - base_de_donnees       : Base de données qui contient les caractères de référence.

        Retourne : La valeur (str) du caractère identifié.

    """

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


    """
        Description : Identifie une étiquette à partir de l’identification de caractères basée sur la distance.

        Arguments :
            - image_etiquette   : Une image qui correspond à une étiquette.
            - base_de_donnees   : Base de données qui contient les caractères de référence.

        Retourne : Une chaîne de caractères qui correspond à la lecture de l’étiquette.

    """

    tableau = decouper(image_etiquette)  # retourne des images en tableau découpé de l'étiquette [a,s,s,y]

    code = str()

    for i in range(0, 13, 1):  # essaye de parcourir le tableau
        code += identifier_caracteres_avec_distances((tableau[i]), base_de_donnees)

    return code


def identifier_caractere_avec_centroides(references_image, reference_centroides):

    """
        Description : Identifie un caractère alphanumérique par rapport à la distance avec un ensemble de centroïdes de référence.

        Arguments :
            - references_image      : L’image du caractère à identifier.
            - reference_centroide   : Un dictionnaire qui contient l'ensemble des centroïdes de référence.

        Retourne : La valeur (str) du caractère identifié.
    """

    if references_image.shape != (40, 40):
        raise ValueError('ESTI DE TARTE')

    distance_minimale = float('inf')
    caractere_identifie = None

    # Parcourir tous les centroïdes de référence
    for caractere, centroide_reference in reference_centroides.items():

        # Extraire les coordonnées x et y du centroïde de référence
        xc_ref, yc_ref = centroide_reference

        # Calculer les coordonnées x et y du centroïde de l'image
        xc, yc = calculer_centroide(references_image)

        # Calculer la distance entre l'image et le centroïde de référence
        distance = ((xc_ref - xc) ** 2 + (yc_ref - yc) ** 2) ** 0.5

        # Mettre à jour le caractère identifié si la distance actuelle est plus petite
        if distance < distance_minimale:
            distance_minimale = distance
            caractere_identifie = caractere

    return caractere_identifie
def lire_etiquette_centroides(image_etiquette, references_centroides):

    """
        Identifie une étiquette à partir de l'identification de caractères basée sur les centroïdes.

        Arguments:
        - image_etiquette: Une image qui correspond à une étiquette.

        Retourne:
        Une chaîne de caractères qui correspond à la lecture de l'étiquette.
    """

    # Initialiser une liste pour stocker les caractères identifiés
    caracteres_identifies = []

    # Parcourir les sous-images de l'étiquette (supposons que l'étiquette soit une grille de caractères)
    for colonne in range(0, image_etiquette.shape[1], 40):
        for ligne in range(0, image_etiquette.shape[0], 40):
            # Extraire la sous-image correspondant à un caractère potentiel
            caractere_image = image_etiquette[ligne:ligne + 40, colonne:colonne + 40]

            # Identifier le caractère à partir des centroïdes (vous devez avoir une fonction appropriée ici)
            identification = identifier_caractere_avec_centroides(caractere_image, references_centroides)

            # Ajouter le caractère identifié à la liste
            caracteres_identifies.append(identification)

    # Concaténer les caractères identifiés pour former l'étiquette complète
    etiquette_lue = ''.join(caracteres_identifies)

    return etiquette_lue
