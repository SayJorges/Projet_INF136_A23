# Librairies internes
from algorithme.algorithme import *
from donnees.donnees import *
from datetime import *


def filtrer_ville():
    """
    filtre les villes en allant chercher les refrences dans les etiquettes.

    Arguments:
        'aucun'

    Retourne:
        un dictionnaire des villes
        """
    # Creation du dictionnaire des villes avec leur numero de references
    t_ville = {'1': 'Laval', '2': 'Longeuil', '3': 'St-Hubert', '4': 'Kitchener', '5': 'Cambridge', '6': 'Springfield',
               '7': 'Wichita', '8': 'Cleveland', '9': 'Nottingham', '0': 'Madrid'}

    etiquette = charger_etiquettes()
    references = charger_references()

    total = {'Laval': 0, 'Longeuil': 0, 'St-Hubert': 0, 'Kitchener': 0, 'Cambridge': 0,
             'Springfield': 0, 'Wichita': 0, 'Cleveland': 0, 'Nottingham': 0, 'Madrid': 0}

    # Boucle pour parcourir chacune des 40 etiquette
    for i in range(40):
        input_str = lire_etiquette_distances(etiquette[i], references)
        dernier_charactere = input_str[-1]
        ville = t_ville[dernier_charactere]
        total[ville] += 1

    return total


def filtrer_part():
    """
    filtre les types (PART) en se basant sur les references.

    Arguments:
        'aucun'

    Retourne:
        un dictionnaire des types PART
        """
    t_ville = {('P', '1'): 'Laval', ('P', '2'): 'Longeuil', ('P', '3'): 'St-Hubert', ('P', '4'): 'Kitchener',
               ('P', '5'): 'Cambridge', ('P', '6'): 'Springfield', ('P', '7'): 'Wichita', ('P', '8'): 'Cleveland',
               ('P', '9'): 'Nottingham', ('P', '0'): 'Madrid'}

    etiquette = charger_etiquettes()
    references = charger_references()

    part = {'Laval': 0, 'Longeuil': 0, 'St-Hubert': 0, 'Kitchener': 0, 'Cambridge': 0,
            'Springfield': 0, 'Wichita': 0, 'Cleveland': 0, 'Nottingham': 0, 'Madrid': 0}

    for i in range(40):
        input_str = lire_etiquette_distances(etiquette[i], references)
        dernier_charactere = input_str[-1]
        premier_charactere = input_str[0]
        ville = t_ville.get((premier_charactere, dernier_charactere), None)

        if ville:
            part[ville] += 1

    return part


def filtrer_assy():
    """
    filtre les types (ASSY) en se basant sur les references.

    Arguments:
        'aucun'

    Retourne:
        un dictionnaire des types ASSY
        """

    t_ville = {('A', '1'): 'Laval', ('A', '2'): 'Longeuil', ('A', '3'): 'St-Hubert', ('A', '4'): 'Kitchener',
               ('A', '5'): 'Cambridge', ('A', '6'): 'Springfield', ('A', '7'): 'Wichita', ('A', '8'): 'Cleveland',
               ('A', '9'): 'Nottingham', ('A', '0'): 'Madrid'}

    etiquette = charger_etiquettes()
    references = charger_references()

    assy = {'Laval': 0, 'Longeuil': 0, 'St-Hubert': 0, 'Kitchener': 0, 'Cambridge': 0,
            'Springfield': 0, 'Wichita': 0, 'Cleveland': 0, 'Nottingham': 0, 'Madrid': 0}

    for i in range(40):
        input_str = lire_etiquette_distances(etiquette[i], references)
        dernier_charactere = input_str[-1]
        premier_charactere = input_str[0]
        ville = t_ville.get((premier_charactere, dernier_charactere), None)

        if ville:
            assy[ville] += 1

    return assy


def generer():
    """
    genere le rapport demandé avec toutes les informations.

    Arguments:
        'aucun'

    Retourne:
        rien
        """

    total = filtrer_ville()
    assy = filtrer_assy()
    part = filtrer_part()

    # obtenir la date et l'heure actuelles
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ouvrir fichier text (fichier avec l'extension .txt) et le mode 'w' pour pouvoir écrire
    with open("generer.txt", 'w') as fichier:
        # écrire dans le rapport la date et l'heure de la génération du rapport
        fichier.write(f"Rapport généré le {current_datetime}\n\n")

        # écrire les en-têtes du tableau
        fichier.write(f"{'Usine': <15}{'ASSY': <15}{'PART': <15}{'TOTAL': <15}\n")
        fichier.write('-' * 60 + '\n')

        # parcourir la liste qui les résultat de l'analyse rapport
        for ville in total:
            # écrire dans le rapport avec le formatage approprié
            # {ville pour nous situer [le résultat]} 'retour'
            # le format utiliser pour fichier.write provient des notes de cours du cours 9 et chatgpt
            line = f"{ville: <15}{assy[ville]: <15}{part[ville]: <15}{total[ville]: <15}\n"
            fichier.write(line)


if __name__ == '__main__':
    generer()
