
# Librairies internes
from images.image import *

# Librairies testées
from etiquettes.etiquette import *

# Constantes internes
CHEMIN_ETIQUETTE_TEST = r'..\..\donnees\etiquettes\1.jpg'


def test_visuel_etiquette_decouper():
   """
   Test visuel de la fonction de découpage.
   """

   # Charger l'étiquette de test
   img = charger_jpeg(CHEMIN_ETIQUETTE_TEST)

   # La découper
   caracteres = decouper(img)

   # Visualiser le résultat du découpage
   for caractere in caracteres:
       afficher(caractere, "Test decouper etiquette", False)
#