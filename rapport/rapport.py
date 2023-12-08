

def creer_dict():

def remplir_dict():


def ecrire():













def generer(dict,):

    DICTIO ={"01":"LAVAL","02":"LONGUEUIL","03":"ST-HUBERT","04":"KITCHENER","05":\
        "CAMBRIDGE","06":"SPRINGFIELD","07":"WICHITA","08":"CLEVELAND","09":"NOTTINGHAM","10":"MADRID"}


    #ouvrir fichier text (fichier avec l'extension .txt) et le mode 'w' pour pouvoir écrire
    with open(rapport_fichier, 'w') as fichier:

        #initialiser compteur
        c_laval_assy = 0
        c_laval_part = 0


        #écrire dans le rapport le nombre d'objet détectés à partir de la longueur de la liste
        fichier.write(f"Nombre d'objets détectés: {len(list_dict)}\n\n\n")
        #parcourir la liste qui les résultat de l'analyse rapport
        for i in list_dict:
            #écrire dans le rapport avec ('text indique le résulat. {i pour nous situer [le résultat] 'retour')
            #le format utiliser pour fichier.write provient des notes de cours du cours 9 et chatgpt
            fichier.write(f"Usine. {t}\n\n")
            fichier.write(f"ASSY: {i['coords']}\n")
            fichier.write(f"PART: {i['x_min']}\n")
            fichier.write(f"TOTAL: {i['x_max']}\n")
            fichier.write(f"y_min: {i['y_min']}\n")
            fichier.write(f"y_max: {i['y_max']}\n")
            fichier.write(f"hauteur: {i['hauteur']}\n")
            fichier.write(f"largeur: {i['largeur']}\n")
            fichier.write(f"angle: {i['angle']}\n\n")
            # Ajout +1 au compteur pour différencier les objets
            nb_objet += 1




if mai