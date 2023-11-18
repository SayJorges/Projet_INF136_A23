
# Librairies g?n?rales
import time

# Librairies internes
from donnees.donnees import *
from images.image import *

# Librairies test?es
from algorithme.algorithme import *


def test_identifier_caractere_distances():
   """
   Test pour l'identification des caract?re sur le jeu de caract?res de r?f?rence bas? sur les distances.
   """

   # Charger les images de r?f?rence
   references = charger_references()

   # Marquer le d?but du test
   debut = time.time()

   # Identifier chacun des caract?res
   for caractere in references:

       # Identifier le caract?re courant
       caractere_identifie = identifier_caractere_avec_distances(references[caractere], references)

       # Valider que le caract?re courant correspond ? la cl? du dictionnaire de r?f?rences
       assert str(caractere_identifie) == caractere

   # Calculer la dur?e du test
   duree = time.time() - debut

   # Afficher la dur?e du test
   print(f'Dur?e: {duree} seconds')


def test_lire_etiquette_distances():
   """
   Test pour la lecture d'une ?tiquette avec l'identification des caract?res bas?e sur la distance.
   """

   # Charger la base de donn?es d'?tiquettes
   references = charger_references()
   etiquettes = charger_etiquettes()
   assert lire_etiquette_distances(etiquettes[0], references) == 'ASSYA20020202'


def test_integration_1():
   """
   Test d'int?gration qui consiste ? l'identification bas? sur la minimisation de la distance.
   """

   # Charger la base de donn?es d'?tiquettes
   etiquettes = charger_etiquettes()

   # Initialiser le compteur d'?tiquettes
   i = 1

   # Analyser chaque ?tiquette et afficher le r?sultat
   for etiquette in etiquettes:

       # Lire l'?tiquette
       etiquette_str = lire_etiquette_distances(etiquette)

       # Afficher l'?tiquette courante
       afficher(etiquette, etiquette_str.upper())

       # Incr?menter le compteur
       i += 1


def test_identifier_caractere_centroides():
   """
   Test pour l'identification des caract?re sur le jeu de caract?res de r?f?rence bas? sur les distances des
   centro?des.
   """

   # Charger les images de référence
   references = charger_references()

   # Charger les centroïdes de reference
   references_centroides = charger_centroides_reference()

   # Marquer le début du test
   debut = time.time()

   # Identifier chacun des caractères
   for caractere in references:

       # Identifier le caractère courant
       caractere_identifie = identifier_caractere_avec_centroides(references[caractere], references_centroides)

       # Valider que le caract?re courant correspond ? la cl? du dictionnaire de r?f?rences
       assert str(caractere_identifie) == caractere

   # Calculer la dur?e du test
   duree = time.time() - debut

   # Afficher la dur?e du test
   print(f'Dur?e: {duree} seconds')


#def test_lire_etiquette_centroides():
#    """
#    Test pour la lecture d'une ?tiquette avec l'identification des caract?res bas?e sur les centro?des.
#    """
#
#    # Charger la base de donn?es d'?tiquettes
#    etiquettes = charger_etiquettes()
#
#    assert lire_etiquette_centroides(etiquettes[0]) == 'ASSYA20020202'
#
#
#def test_integration_2():
#    """
#    Test d'int?gration qui consiste ? l'identification bas? sur la distance des centro?des.
#    """
#
#    # Charger la base de donn?es d'?tiquettes
#    etiquettes = charger_etiquettes()
#
#    # Initialiser le compteur d'?tiquettes
#    i = 1
#
#    # Analyser chaque ?tiquette et afficher le r?sultat
#    for etiquette in etiquettes:
#
#        # Lire l'?tiquette
#        etiquette_str = lire_etiquette_centroides(etiquette)
#
#        # Afficher l'?tiquette courante
#        afficher(etiquette, etiquette_str.upper())
#
#        # Incr?menter le compteur
#        i += 1
#