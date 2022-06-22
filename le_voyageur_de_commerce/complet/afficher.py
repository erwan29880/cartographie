import pandas as pd
import tkinter as tk
import numpy as np
import param
from tsp_ga import TSP_GA





class Afficher:

    """
    classe pour afficher les coordonnées des points définis dans la classe Graphe
    et afficher le chemin heuristique défini par la matrice_od dans la classe Graph
    """


    def __init__(self, distance, route_heur, qgis):
        self.largeur_fenetre = param.LARGEUR + 20
        self.hauteur_fenetre = param.HAUTEUR + 100
        self.padding = 10
        self.distance = distance
        self.coordonnees = pd.read_csv(param.LIEUX_CSV)
        self.route_heuristique = route_heur
        self.couleur = ['yellow','purple','pink','orange', 'black', 'gray', ]
        self.increment = 0
        self.coordoonees_heuristiques = pd.read_csv(param.LIEUX_CSV_HEURISTIQUE)
        self.root = tk.Tk()
        self.root.title("groupe 2")
        self.root.geometry(str(self.largeur_fenetre)+'x'+str(self.hauteur_fenetre))
        self.root.minsize(param.LARGEUR,param.HAUTEUR)
        self.root.configure(bg="white") 
        self.root.resizable(width=True, height=True)
        tk.Label(self.root, text='Voyageur de commerce', font=("Helvetica", 20), fg='black').pack()
        self.canvas = tk.Canvas(self.root, width = param.LARGEUR, height=param.HAUTEUR, bg="white")
        self.canvas.pack(side=tk.TOP, ipadx=self.padding, ipady=self.padding)
        tk.Label(text="Appuyer sur <échap> pour quitter, <a> pour optimiser la route").pack()
        self.distancetexte = tk.StringVar()
        self.affiche_distance = tk.Label(self.root, textvariable=self.distancetexte).pack()
        self.qgis = qgis

    def exit(self, event):
        self.root.destroy()


    def tracer_cercle(self, x, y, couleur = 'purple', rayon=9, remplissage=True, valeur='2'):
        x1 = x - rayon
        x2 = x + rayon
        y1 = y - rayon 
        y2 = y + rayon 

        self.canvas.create_text (x , y , text=valeur)

        if remplissage == False:
            return self.canvas.create_oval(x1, y1, x2, y2, outline=couleur, fill='')
        else:
            return self.canvas.create_oval(x1, y1, x2, y2, outline=couleur, fill=couleur)


    def tracer_ligne(self, x1, y1, x2, y2, couleur='green', width=2):
        self.canvas.create_line(x1, y1, x2, y2, fill=couleur, width=width)



    def dessiner(self):
    # tracer les 'villes'

        if self.qgis == True:
            for i in range(self.coordonnees.shape[0]):

                abs = self.coordonnees.iloc[i, 0]
                ord = self.coordonnees.iloc[i, 1]

                abs = str(np.round(float(abs), 3)*1000)
                ord = str(np.round(np.abs(float(ord)),3)*10000)
                
                
                abs = int(abs[2:5])
                ord = int(ord[1:4])


                if i==0:  # --> afficher le point de départ
                    self.tracer_cercle(abs, ord, couleur='red', rayon=14, remplissage=False)
                else:
                    self.tracer_cercle(abs, ord,remplissage=False)

            # tracer le chemin heuristique
            for i in range(self.coordoonees_heuristiques.shape[0]-1):
                abs1 = self.coordoonees_heuristiques.iloc[i,0]
                ord1 = self.coordoonees_heuristiques.iloc[i, 1]
                abs2 = self.coordoonees_heuristiques.iloc[i+1, 0]
                ord2 = self.coordoonees_heuristiques.iloc[i+1, 1]

                # choix d'une échelle pour afficher les coordonnées de QGIS
                abs1 = str(np.round(float(abs1), 3)*1000)
                ord1 = str(np.round(np.abs(float(ord1)),3)*10000)
                abs1 = int(abs1[2:5])
                ord1 = int(ord1[1:4])
                abs2 = str(np.round(float(abs2), 3)*1000)
                ord2 = str(np.round(np.abs(float(ord2)),3)*10000)
                abs2 = int(abs2[2:5])
                ord2 = int(ord2[1:4])



                if i==0:  # --> afficher le sens de la tournée
                    self.tracer_ligne(abs1, ord1, abs2, ord2, width=5, couleur='red')
                else:
                    self.tracer_ligne(abs1, ord1, abs2, ord2)

        else:
            for i in range(self.coordonnees.shape[0]):
                if i==0:  # --> afficher le point de départ
                    self.tracer_cercle(self.coordonnees.iloc[i, 0], self.coordonnees.iloc[i, 1], couleur='red', rayon=9,remplissage=False, valeur=str(i))
                else:
                    self.tracer_cercle(self.coordonnees.iloc[i, 0], self.coordonnees.iloc[i, 1],remplissage=False,valeur=str(i))

            # tracer le chemin heuristique
            for i in range(self.coordoonees_heuristiques.shape[0]-1):
                x1 = self.coordoonees_heuristiques.iloc[i,0]
                y1 = self.coordoonees_heuristiques.iloc[i, 1]
                x2 = self.coordoonees_heuristiques.iloc[i+1, 0]
                y2 = self.coordoonees_heuristiques.iloc[i+1, 1]

                if i==0:  # --> afficher le sens de la tournée
                    self.tracer_ligne(x1, y1, x2, y2, width=5, couleur='red')
                else:
                    self.tracer_ligne(x1, y1, x2, y2)
            


    def dessiner_chemin_optimise(self, df):
        self.canvas.delete('all')

        if self.qgis == True:
            # tracer le chemin heuristique
            for i in range(df.shape[0]-1):
                abs1 = df.iloc[i,0]
                ord1 = df.iloc[i, 1]
                abs2 = df.iloc[i+1, 0]
                ord2 = df.iloc[i+1, 1]

                # choix d'une échelle pour afficher les coordonnées de QGIS               
                abs1 = str(np.round(float(abs1), 3)*1000)
                ord1 = str(np.round(np.abs(float(ord1)),3)*10000)
                abs1 = int(abs1[2:5])
                ord1 = int(ord1[1:4])
                abs2 = str(np.round(float(abs2), 3)*1000)
                ord2 = str(np.round(np.abs(float(ord2)),3)*10000)
                abs2 = int(abs2[2:5])
                ord2 = int(ord2[1:4])


                if i==0:  # --> afficher le point de départ
                    self.tracer_cercle(abs1, ord1, couleur='red', rayon=14,remplissage=False, valeur=str(i))
                else:
                    self.tracer_cercle(abs1, ord1,remplissage=False, valeur=str(i))

                if i==0:  # --> afficher le sens de la tournée
                    self.tracer_ligne(abs1, ord1, abs2, ord2, width=5, couleur='red')
                    self.increment = self.increment + 1
                else:
                    if self.increment == len(self.couleur):
                        self.increment = 0
                    
                    col = self.couleur[self.increment] 
                    self.tracer_ligne(abs1, ord1, abs2, ord2, couleur=col)

        else:
            # tracer le chemin heuristique
            for i in range(df.shape[0]-1):
                x1 = df.iloc[i,0]
                y1 = df.iloc[i, 1]
                x2 = df.iloc[i+1, 0]
                y2 = df.iloc[i+1, 1]


                if i==0:  # --> afficher le point de départ
                    self.tracer_cercle(x1,y1, couleur='red', rayon=14, remplissage=False, valeur=str(i))
                else:
                    self.tracer_cercle(x1, y1,remplissage=False, valeur=str(i))

                if i==0:  # --> afficher le sens de la tournée
                    self.tracer_ligne(x1, y1, x2, y2, width=5, couleur='red')
                    self.increment = self.increment + 1
                else:
                    if self.increment == len(self.couleur):
                        self.increment = 0
                    
                    col = self.couleur[self.increment] 
                    self.tracer_ligne(x1, y1, x2, y2, couleur=col)


                



    def lancer_algo_ga(self):

        """
        lancer l'algorithme génétique
        """


        cls_ga = TSP_GA(self.route_heuristique, self.distance)
        reponse = cls_ga.run(10)               
        self.distance = reponse[0]                  # distance
        self.route_heuristique = reponse[3]         # route
        df = reponse[2]                             # en dataframe
        self.dessiner_chemin_optimise(df)
        var = str(np.round(self.distance/1000, 2)) + ' kms'
        self.distancetexte.set(var)
        # récupérer le chemin optimisé dans un fichier txt
        with open(param.ROUTE_OPTIMISEE, 'w') as f:
            string = ""
            for i in self.route_heuristique:
                string = string + str(i) + ','
            f.write(string)
            
   
    def ouvrir_fenetre(self):
        self.dessiner()
        self.root.bind("<a>", lambda x: self.lancer_algo_ga())
        self.root.bind("<Escape>", lambda x: self.root.destroy())
        self.root.mainloop()