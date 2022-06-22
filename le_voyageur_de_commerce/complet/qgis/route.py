import numpy as np
import random
import time
import pandas as pd
from graph import Graph
import param

class Route:


    """
    crée un chemin aléatoire, calcule la distance de ce chemin
    """

    def __init__(self):
        self.ordre = [0]
        self.distance = 0
               


    def creer_liste(self):

        # créer une liste vide
        temp = []

        for i in range(1, param.NB_LIEUX):
            temp.append(i)

        random.shuffle(temp)
        self.ordre = self.ordre + temp
        self.ordre.append(0)


    def calcul_distance_route(self, matrice):
       
        self.creer_liste()
                
        for i in range(len(self.ordre) - 1):

            x = self.ordre[i]
            y = self.ordre[i+1]
            self.distance = self.distance + matrice.iloc[x, y]
            

        return self.distance, self.ordre


        


if __name__ == "__main__":

    cls = Route()

    # instancier la classe Graph pour obtenir une matrice_od (origine distance)
    cls_graph = Graph()
 
    # récupérer matrice_od
    _, matrice_od = cls_graph.main_graph()
    
    print(matrice_od)
    distance, ordre = cls.calcul_distance_route(matrice_od)

    print(distance)
    print(ordre)
    
    
