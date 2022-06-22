import pandas as pd
import numpy as np
import param


class Mat_od:

    """
    Récupérer le csv matrice_od provenant de qgis, et le mettre en forme pour exploitation par l'application
    """


    def __init__(self, path_csv=param.CSV_QGIS):
        self.df = pd.read_csv(path_csv) 
        self.lieux = None

    def process(self):
        self.df = self.df.drop(columns=['fid', 'cat'], axis=1)
        self.df['from_cat'] = self.df['from_cat']-1   # les index partent de 1, donc on soustrait
        self.df['to_cat'] = self.df['to_cat']-1       # les index partent de 1, donc on soustrait
        
        # enregistrer le nombre de lieux, pour que param.py le récupère
        self.lieux = sorted(list(self.df['from_cat'].unique()))
        with open('./csv/nombre_de_lieux.txt', 'w') as f:
            f.write(str(len(self.lieux)))
        
        self.df = self.df.drop_duplicates()  # enlenver les lignes dupliquées
        self.df = self.df.sort_values(by='from_cat')
        self.df = self.df.reset_index(drop=True)


    def main(self, rec_csv=False):

        """
        mettre le dataframe au format voulu
        """

        self.process()

        dico = {}
        for num in self.lieux:
            df_prov0 = self.df[self.df['from_cat'] == num]
            df_prov0 = pd.concat((df_prov0, pd.DataFrame(np.array([[num, num, 0]]), columns=list(self.df.columns))), ignore_index=True)
            df_prov = df_prov0.sort_values(by='to_cat')
            dico[num] = list(df_prov['cost'])
            
        matrice_od_from_qgis = pd.DataFrame(dico, columns=self.lieux)

        if rec_csv==True:
            matrice_od_from_qgis.to_csv(param.ADRESSE_FICHIER_CSV_QGIS_PROCESSED, index=False)

        return matrice_od_from_qgis
        
if __name__ == '__main__':

    cls = Mat_od()
    print(cls.main(rec_csv=True))
    