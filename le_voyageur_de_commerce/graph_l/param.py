import os
import pandas as pd

# ------------------------------------------------------------------------
# pour les fichiers de Laurent, renseigner LIEUX_CSV ligne 18
# pour générer des lieux aléatoires, commenter la ligne 33 et décommenter la ligne 34, et renseigner une adresse de sortie pour LIEUX_CSV ligne 18


CSV_QGIS = "./csv/od_csv1.csv"
ADRESSE_FICHIER_CSV_QGIS_PROCESSED = "./csv/matrice_od_qgis.csv"
LIEUX_CSV_QGIS_PROCESSED = "./csv/liste_lieux_qgis_processed.csv"
LIEUX_CSV_QGIS = "./csv/liste_lieux_qgis.csv"

# fichier créé par lieu_qgis.py
if os.path.exists(LIEUX_CSV_QGIS_PROCESSED):
    LIEUX_CSV = LIEUX_CSV_QGIS_PROCESSED
else:
    LIEUX_CSV = "./csv/graph_10.csv"


# fichier créé par matrice_qgis.py
if os.path.exists(ADRESSE_FICHIER_CSV_QGIS_PROCESSED):
    ADRESSE_FICHIER_CSV = ADRESSE_FICHIER_CSV_QGIS_PROCESSED
else:
    ADRESSE_FICHIER_CSV = "./csv/matrice_od.csv"


# fichier créé par matrice_qgis.py
if os.path.exists('./csv/nombre_de_lieux.txt'):
    with open('./csv/nombre_de_lieux.txt', 'r') as f:
        NB_LIEUX = int(f.read())
else:
    NB_LIEUX = int(pd.read_csv(LIEUX_CSV).shape[0])
    # NB_LIEUX = 50

print(NB_LIEUX)




LIEUX_CSV_HEURISTIQUE = "./csv/liste_lieux_heuristique.csv"
ROUTE_OPTIMISEE = "./csv/route_optimisee.txt"


PRECISION_DISTANCE_EUCLIDIENNE = 7  # une précision trop faible a de fortes chances de générer des erreurs dans Graph.heuristique()
PRECISION_GEO = 3                   # précision des coordonnées x y
LARGEUR = 800
HAUTEUR = 600
GENES_A_MUTER = 4

