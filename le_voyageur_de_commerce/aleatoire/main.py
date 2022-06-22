import afficher
import graph
import route
import pandas as pd
import numpy as np
import param
import lieu_qgis
import matrice_qgis

def main(apport_csv_qgis=True, creer_lieux=False):

    cls_graph = graph.Graph(creer_lieux_aleatoires=creer_lieux)

    if apport_csv_qgis == True:
        cls_lieu = lieu_qgis.Lieu_qgis().main(rec_csv=True)
        cls_matrice = matrice_qgis.Mat_od().main(rec_csv=True)
        route, distance = cls_graph.heuristique()
        # heuristique de départ : 
        route, distance = cls_graph.heuristique()


        # affichage
        fenetre = afficher.Afficher(str(distance), route, qgis=True)
        fenetre.ouvrir_fenetre()


    else:               
        
        cls_graph.main_graph()

        # heuristique de départ : 
        route, distance = cls_graph.heuristique()


        # affichage
        fenetre = afficher.Afficher(str(distance), route, qgis=False)
        fenetre.ouvrir_fenetre()



main(apport_csv_qgis=False, creer_lieux=True)