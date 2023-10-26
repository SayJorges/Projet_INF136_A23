
# Librairies générales
import time

# Librairies internes
from donnees.donnees import *
from images.image import *

# Librairies testées
from algorithme.algorithme import *


#def test_identifier_caractere_distances():
#    """
#    Test pour l'identification des caractère sur le jeu de caractères de référence basé sur les distances.
#    """
#
#    # Charger les images de référence
#    references = charger_references()
#
#    # Marquer le début du test
#    debut = time.time()
#
#    # Identifier chacun des caractères
#    for caractere in references:
#
#        # Identifier le caractère courant
#        caractere_identifie = identifier_caractere_avec_distances(references[caractere], references)
#
#        # Valider que le caractère courant correspond à la clé du dictionnaire de références
#        assert str(caractere_identifie) == caractere
#
#    # Calculer la durée du test
#    duree = time.time() - debut
#
#    # Afficher la durée du test
#    print(f'Durée: {duree} seconds')
#
#
#def test_lire_etiquette_distances():
#    """
#    Test pour la lecture d'une étiquette avec l'identification des caractères basée sur la distance.
#    """
#
#    # Charger la base de données d'étiquettes
#    references = charger_references()
#    etiquettes = charger_etiquettes()
#    assert lire_etiquette_distances(etiquettes[0], references) == 'ASSYA20020202'
#
#
#def test_integration_1():
#    """
#    Test d'intégration qui consiste à l'identification basé sur la minimisation de la distance.
#    """
#
#    # Charger la base de données d'étiquettes
#    etiquettes = charger_etiquettes()
#
#    # Initialiser le compteur d'étiquettes
#    i = 1
#
#    # Analyser chaque étiquette et afficher le résultat
#    for etiquette in etiquettes:
#
#        # Lire l'étiquette
#        etiquette_str = lire_etiquette_distances(etiquette)
#
#        # Afficher l'étiquette courante
#        afficher(etiquette, etiquette_str.upper())
#
#        # Incrémenter le compteur
#        i += 1
#
#
#def test_identifier_caractere_centroides():
#    """
#    Test pour l'identification des caractère sur le jeu de caractères de référence basé sur les distances des
#    centroïdes.
#    """
#
#    # Charger les images de référence
#    references = charger_references()
#
#    # Charger les centroïdes de référence
#    references_centroides = charger_centroides_reference()
#
#    # Marquer le début du test
#    debut = time.time()
#
#    # Identifier chacun des caractères
#    for caractere in references:
#
#        # Identifier le caractère courant
#        caractere_identifie = identifier_caractere_avec_centroides(references[caractere], references_centroides)
#
#        # Valider que le caractère courant correspond à la clé du dictionnaire de références
#        assert str(caractere_identifie) == caractere
#
#    # Calculer la durée du test
#    duree = time.time() - debut
#
#    # Afficher la durée du test
#    print(f'Durée: {duree} seconds')
#
#
#def test_lire_etiquette_centroides():
#    """
#    Test pour la lecture d'une étiquette avec l'identification des caractères basée sur les centroïdes.
#    """
#
#    # Charger la base de données d'étiquettes
#    etiquettes = charger_etiquettes()
#
#    assert lire_etiquette_centroides(etiquettes[0]) == 'ASSYA20020202'
#
#
#def test_integration_2():
#    """
#    Test d'intégration qui consiste à l'identification basé sur la distance des centroïdes.
#    """
#
#    # Charger la base de données d'étiquettes
#    etiquettes = charger_etiquettes()
#
#    # Initialiser le compteur d'étiquettes
#    i = 1
#
#    # Analyser chaque étiquette et afficher le résultat
#    for etiquette in etiquettes:
#
#        # Lire l'étiquette
#        etiquette_str = lire_etiquette_centroides(etiquette)
#
#        # Afficher l'étiquette courante
#        afficher(etiquette, etiquette_str.upper())
#
#        # Incrémenter le compteur
#        i += 1
#