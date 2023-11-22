from images.image import *
from constantes import *

def exemple1():
    lettre = 'F'
    mon_image = charger_jpeg(CHEMIN_REFERENCES+"\\F.jpg")
    afficher(mon_image)

def exemple2():
    for symbol in REFERENCE_LETTRES_CHIFFRES:
       print(symbol)
def exemple3():
    dictio = {}
    dictio['a']=1
    dictio['b']=2
    dictio['c']=3
    dictio['d']=4
    dictio['e']=5
    for cle in dictio.keys():
    #   print(cle)
        print(dictio[cle])

if __name__ == "__main__":
    #exemple1()
    exemple2()
   # exemple3()
