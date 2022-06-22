import param
import pandas as pd
import numpy as np
import random
import graph

class TSP_GA:



    def __init__(self, route_heuristique, distance_heurstique):
        self.coordoonees_heuristiques = pd.read_csv(param.LIEUX_CSV_HEURISTIQUE)
        self.matrice_od = np.array(pd.read_csv(param.ADRESSE_FICHIER_CSV))
        self.route_heuristique = route_heuristique
        # self.distance_heuristique = distance_heurstique
        self.route_test = []
        self.distance_test = 0
        self.tableau_route = []
        self.tableau_distance = []


    def mutate(self, road):

        """
        mute deux éléments de la route heuristique
        """


        n1 = random.randint(1, (param.NB_LIEUX-1))
        liste = [x for x in range(1, (param.NB_LIEUX))]
        liste.remove(n1)
        n2 = random.randint(1, (param.NB_LIEUX-1))

        truc = road.copy()
        truc[n1], truc[n2] = truc[n2], truc[n1]

        return truc
        



    def crossing(self, road, inter=True):

        """
        déplace un ensemble de gènes
        """

        n1 = random.randint(1, (param.NB_LIEUX-1))
        liste = [x for x in range(1, (param.NB_LIEUX))]
        liste.remove(n1)
        n2 = random.randint(1, (param.NB_LIEUX-1))

        truc = road.copy()
        truc[n1], truc[n2] = truc[n2], truc[n1]

        if inter == True:
            truc2 = truc[1:-1].copy()
            x1 = random.randint(0, len(truc2))
            parent2 = [0] + truc2[x1:].copy() + truc2[0:x1].copy() + [0]
            return parent2, self.distance(parent2)

        else:    
            return truc, self.distance(truc)

        
    def lieux(self, route):
        df = pd.read_csv(param.LIEUX_CSV)
        liste = []
        for i in route:
            xx = df.iloc[i,0]
            yy = df.iloc[i, 1]
            liste.append([xx, yy])        
        return pd.DataFrame(liste, columns=['x', 'y'])
        


    

    def run(self, nbre_iter):
        
        """
        while repart de la route heuristique à chaque itération
        for calcule 5 enfants mutants
        """

        distance_h = self.distance(self.route_heuristique)
        i = 0

        while i < nbre_iter: 

            self.route_test, self.distance_test = self.crossing(self.route_heuristique)

            for i in range(5):
                self.route_test, self.distance_test  = self.crossing(self.route_test)
                if self.distance_test < distance_h:
                    
                    return self.distance_test, distance_h, self.lieux(self.route_test), self.route_test

            if self.distance_test < distance_h:
                    return self.distance_test, distance_h, self.lieux(self.route_test), self.route_test
            
            i = i+1

        return False
           

    def distance(self, liste_a_tester):

        """
        retourne la distance de la route
        """

        distance_enfant = [self.matrice_od[liste_a_tester[x], liste_a_tester[x+1]] for x in liste_a_tester[:-2]]
        distance_enfant.append(self.matrice_od[param.NB_LIEUX-1,0])
        return np.sum(distance_enfant)





if __name__ == "__main__":

    cls_graph = graph.Graph()

    # heuristique de départ : 
    route, distance = cls_graph.heuristique()
    cls_ga = TSP_GA(route, distance)
    
    
    mini = cls_ga.run(10)

    print(mini[0])
    print(mini[3])
   
    for i in range(10):
        try:    
            cls_ga = TSP_GA(mini[3], mini[0])
            mini = cls_ga.run(10)

            print(mini[0])
            print(mini[3])
        except:
            continue
            
