from algorithme.algorithme import *

# Librairies internes
from donnees.donnees import *
from images.image import *


def filtrer_ville():
    t_ville = {'1': 'Laval', '2': 'Longeuil', '3': 'St-Hubert', '4': 'Kitchener', '5': 'Cambridge', '6': 'Springfield',
               '7': 'Witchita', '8': 'Cleveland',
               '9': 'Nottingham', '0': 'Madrid'}

    etiquette = charger_etiquettes()
    references = charger_references()

    result = {'Laval': 0, 'Longeuil': 0, 'St-Hubert': 0, 'Kitchener': 0, 'Cambridge': 0,
              'Springfield': 0, 'Witchita': 0, 'Cleveland': 0, 'Nottingham': 0, 'Madrid': 0}

    for i in range(40):
        input_str = lire_etiquette_distances(etiquette[i], references)
        dernier_charactere = input_str[-1]
        ville = t_ville[dernier_charactere]
        result[ville] += 1
    print(f'{result}')
    return result


def filtrer_type():

    t_type = {'P': 'PART', 'A': 'ASSY'}

    etiquette = charger_etiquettes()
    references = charger_references()

    for i in range(40):

        input_str = lire_etiquette_distances(etiquette[i], references)

        premier_charactere = input_str[0]
        # stocker les ville

        type = t_type[premier_charactere]

        print(f'{type}')


def nb_assy():


    ville_counts = filtrer_ville()

    total_assy = sum(ville_counts.values())
    print(f'{total_assy}')
    return {'Total_assy': total_assy}


# def dict_parts():
#
#
# def generer():
#
#     #ouvrir fichier text (fichier avec l'extension .txt) et le mode 'w' pour pouvoir écrire
#     with open(generer, 'w') as fichier:
#
#         list_dict1 = nb_assy()
#         list_dict2 = nb_part()
#         #écrire dans le rapport le nombre d'objet détectés à partir de la longueur de la liste
#         fichier.write(f"Nombre d'objets détectés: {len(list_dict)}\n\n\n")
#         #parcourir la liste qui les résultat de l'analyse rapport
#         for i in list_dict1:
#             for j in list_dict2:
#             #écrire dans le rapport avec ('text indique le résulat. {i pour nous situer [le résultat] 'retour')
#             #le format utiliser pour fichier.write provient des notes de cours du cours 9 et chatgpt
#             fichier.write(f"Usine\t \t \t ASSY\t\t\t PART\t\t\t TOTAL\n\n")
#             fichier.write(f"Laval: {i['Laval_assy']}{j['Laval_part']}\n")
#             fichier.write(f"Longeuil: {i['Longeuil_assy']}{j['Longeuil_part']}\n")
#             fichier.write(f"St-Hubert: {i['St-Hubert_assy']}{j['St-Huber_part']}\n")
#             fichier.write(f"Kitchener: {i['Kitchener_assy']}{j['Kitchener_part']}\n")
#             fichier.write(f"Cambridge: {i['Cambridge_assy']}{j['Cambridge_part']}\n")
#             fichier.write(f"Springfield: {i['Springfield_assy']}{j['Springfield_part']}\n")
#             fichier.write(f"Witchita: {i['Witchita_assy']}{j['Witchita_part']}\n")
#             fichier.write(f"Cleveland: {i['Cleveland_assy']}{j['Cleveland_part']}\n")
#             fichier.write(f"Nottingham: {i['Nottingham_assy']}{j['Nottingham_part']}\n")
#             fichier.write(f"Madrid: {i['Madrid_assy']}{j['Madrid_part']}\n")
#             # Ajout +1 au compteur pour différencier les objets
#             nb_objet += 1
#
#
#

if __name__ == '__main__':
    filtrer_ville()
