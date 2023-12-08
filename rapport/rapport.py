

def creer_dict():
    etiquette = charger etiquette
    dict ={}
    dicti.append(etiquette)

def nb_assy():

    for i in dict:
        for j in range(0,5)
            if

def nb_part():











def generer():

    #ouvrir fichier text (fichier avec l'extension .txt) et le mode 'w' pour pouvoir écrire
    with open(generer, 'w') as fichier:

        list_dict1 = nb_assy()
        list_dict2 = nb_part()
        #écrire dans le rapport le nombre d'objet détectés à partir de la longueur de la liste
        fichier.write(f"Nombre d'objets détectés: {len(list_dict)}\n\n\n")
        #parcourir la liste qui les résultat de l'analyse rapport
        for i in list_dict1:
            for j in list_dict2:
            #écrire dans le rapport avec ('text indique le résulat. {i pour nous situer [le résultat] 'retour')
            #le format utiliser pour fichier.write provient des notes de cours du cours 9 et chatgpt
            fichier.write(f"Usine\t \t \t ASSY\t\t\t PART\t\t\t TOTAL\n\n")
            fichier.write(f"Laval: {i['Laval_assy']}{j['Laval_part']}\n")
            fichier.write(f"Longeuil: {i['Longeuil_assy']}{j['Longeuil_part']}\n")
            fichier.write(f"St-Hubert: {i['St-Hubert_assy']}{j['St-Huber_part']}\n")
            fichier.write(f"Kitchener: {i['Kitchener_assy']}{j['Kitchener_part']}\n")
            fichier.write(f"Cambridge: {i['Cambridge_assy']}{j['Cambridge_part']}\n")
            fichier.write(f"Springfield: {i['Springfield_assy']}{j['Springfield_part']}\n")
            fichier.write(f"Witchita: {i['Witchita_assy']}{j['Witchita_part']}\n")
            fichier.write(f"Cleveland: {i['Cleveland_assy']}{j['Cleveland_part']}\n")
            fichier.write(f"Nottingham: {i['Nottingham_assy']}{j['Nottingham_part']}\n")
            fichier.write(f"Madrid: {i['Madrid_assy']}{j['Madrid_part']}\n")
            # Ajout +1 au compteur pour différencier les objets
            nb_objet += 1




if mai