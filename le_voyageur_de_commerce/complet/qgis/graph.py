import numpy as np
import pandas as pd
import random
import param




class Graph:

    def __init__(self, creer_lieux_aleatoires=False):
        
        self.liste_lieux = []
        self.matrice_od = None
        self.creer_lieux_aleatoires = creer_lieux_aleatoires

        

    
    def add_lieu(self, largeur=param.LARGEUR, hauteur=param.HAUTEUR, multiple=True):
        
        """
        définit un lieu aléatoire (multiple == false) ou plusieurs selon le nombre de lieux défini par param.NB_LIEUX
        TODO: cette fonction nécessite un ajustement du fichier param.py (NB_LIEUX)
        Créé des coordonnées au hasard
        """

        if multiple==False:
        
            x = round(random.uniform(0,largeur), param.PRECISION_GEO)
            y  = round(random.uniform(0,hauteur), param.PRECISION_GEO)
            self.liste_lieux.append((x,y))

        else:
            
            for i in range(param.NB_LIEUX):
                x = round(random.uniform(0,largeur), param.PRECISION_GEO)
                y  = round(random.uniform(0,hauteur), param.PRECISION_GEO)
                self.liste_lieux.append((x,y))




    
    def euclidien(self, row1, row2):
        
        """
        calcul de la distance euclidienne entre deux vecteurs
        """


        row1 = np.array(row1)
        row2 = np.array(row2)
        
        row1 = row1.reshape(row1.shape[0], 1)
        row2 = row2.reshape(row2.shape[0], 1)
        
        res = (row1 - row2)**2
        res = sum(res)
        res = np.sqrt(res)
        res = np.around(res,param.PRECISION_DISTANCE_EUCLIDIENNE)
        
        return res[0]





    def plus_proches_voisins(self, numero_ligne, return_dict = False):
        
        """
        définit les plus proches voisins d'une ligne d'un dataframe
        retourne un dictionnaire ou une liste
        """

        if self.creer_lieux_aleatoires == True:
            #mise en dataframe pour utiliser les fonctions pandas
            dataframe = np.array(self.liste_lieux)
            dataframe = pd.DataFrame(dataframe, columns=['x', 'y'])
        else:
            dataframe = pd.read_csv(param.LIEUX_CSV)

        row = dataframe.iloc[numero_ligne]
        liste = {}
        
        
        for ligne in range(dataframe.shape[0]):
            
            res = self.euclidien(row, dataframe.iloc[ligne])
            
        
            # définir un nom de variable incrémenté
            mon_nom_de_colonne = str(ligne)
            mon_nom_de_colonne = 'distance_ligne_' + mon_nom_de_colonne
            
            liste[mon_nom_de_colonne] = res        
        
        if return_dict == True:
            return liste
        else:
            liste2 = []
            for i in liste.values():
                liste2.append(i)
            return liste2


    def sauvegarder_csv(self, nom_du_fichier):
            
        """
        enregistrer les coordonnées des lieux en csv
        """

        liste_lieux_to_numpy = np.array(self.liste_lieux)
        numpy_to_df = pd.DataFrame(liste_lieux_to_numpy, columns=['x', 'y'])
        numpy_to_df.to_csv(nom_du_fichier, index=False)




    def calcul_matrice_cout_od(self):
        
        """
        initialise un dictionnaire pour stocker les distances entre chaque ligne du dataframe
        retourne un dataframe 
        """

        dico = dict()

        for i in range(param.NB_LIEUX):
            dico[i] = self.plus_proches_voisins(i)
        
        
        self.matrice_od = pd.DataFrame.from_dict(dico)




    def main_graph(self, creer_lieux=False):

        """
        crée lieux, matrices et fichiers csv
        """

        if self.creer_lieux_aleatoires == True:
            self.add_lieu()
            self.calcul_matrice_cout_od()
            self.sauvegarder_csv(param.LIEUX_CSV)

        else:
            self.calcul_matrice_cout_od()

        
        self.matrice_od.to_csv(param.ADRESSE_FICHIER_CSV, index=False)
        
        return  self.liste_lieux, self.matrice_od



    def heuristique(self):
    
        """
        retourne une route heuristique
        aboutira à une erreur en cas de valeurs identiques dans une rangée
        """



        # récupérer la matrice_od(csv) initialiser les listes 
        data = np.array(pd.read_csv(param.ADRESSE_FICHIER_CSV))
        route = [0]                       # premier point du voyage : 0
        distance = [0.0] 

        # début :
        indice = np.argsort(data[0])[1]   # ! le premier élément de argsort est 0.0 donc on prend le deuxième
        distance.append(data[0][indice])  # récupérer la valeur de la distance de la ligne 0 à l'index trouvé 
        route.append(indice)              # l'indice est la prochaine étape du voyage


        # ni début ni fin

        for lieu in range(param.NB_LIEUX -2):
            indice = route[-1]            # récupérer la dernière 'étape' de la route

            # trouver les valeurs dans la ligne suivant les index (étapes) de route
            prov = []
            for i in range(len(route)):     
                prov.append(data[indice][route[i]])


            indices_utilises = np.setdiff1d(data[indice], prov)     # les valeurs qu'on peut utiliser, enlève les autres
            indice_min = np.sort(indices_utilises)[0]               # trouve le plus proche voisin
            where = np.where(data[indice] == indice_min)[0][0]      # trouve l'index (la localisation) de ce plus proche voisin
            distance.append(data[indice][where])                    # ajoute la distance de l'étape
            route.append(where)                                     # ajoute l'adresse à route


        # fin --> retour à l'étape 0
        distance.append(data[route[-1]][0])
        route.append(0)


        # enregistrer le chemin ré-organisé en csv
        df = pd.read_csv(param.LIEUX_CSV)
        liste = []
        for i in route:
            xx = df.iloc[i,0]
            yy = df.iloc[i, 1]
            liste.append([xx, yy])        
        dat = pd.DataFrame(liste, columns=['x', 'y'])
        dat.to_csv(param.LIEUX_CSV_HEURISTIQUE, index=False)




        return route, sum(distance)



if __name__== '__main__':

    # initialisation de la classe
    cls = Graph(creer_lieux_aleatoires=False)
    
    cls.main_graph()

    route, distance = cls.heuristique()

   

    print(route)
    print(distance)
    