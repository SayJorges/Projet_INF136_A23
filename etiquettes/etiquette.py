from donnees.donnees import *


def decouper(image_etiquette):
    """
        Description : Découpe chacun des caractères d’une étiquette.

        Arguments : Une image qui correspond à une étiquette.

        Retourne : Une liste qui contient les 13 caractères sous la forme d’images en tableaux NumPy.
    """
    #creation d'une liste vide
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


def decouper(image_etiquette):
    """
        Description : Découpe chacun des caractères d’une étiquette.

        Arguments : Une image qui correspond à une étiquette.

        Retourne : Une liste qui contient les 13 caractères sous la forme d’images en tableaux NumPy.
    """

    # Liste pour stocker les images des étiquettes
    images_etiquettes = []
    # boucle pour separer en  13 images de 40 caracteres
    for i in range(0, 13, 1):
        images = image_etiquette[0:40, i * 40:(i * 40 + 40)]
        images_etiquettes.append(images)

    return images_etiquettes
