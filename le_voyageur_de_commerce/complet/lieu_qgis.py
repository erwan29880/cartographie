import pandas as pd
import numpy as np
import param

class Lieu_qgis:

    """
    prend en entrée un csv avec les adresses provenant de QGIS
    retourne un csv au format demandé par l'application
    """


    def __init__(self, path_csv=param.LIEUX_CSV_QGIS):
        self.df = pd.read_csv(path_csv)


    def main(self, rec_csv=False):

        """
        séparer latitude et longitude du fichier d'adresses issu de QGIS
        """

        x, y = [], []

        for i in self.df['latlong']:

            x.append(i.split(',')[0])
            y.append(i.split(',')[1])

            data = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])

        if rec_csv == True:
            data.to_csv(param.LIEUX_CSV_QGIS_PROCESSED, index=False)

        return data

    

if __name__ == '__main__':
    cls = Lieu_qgis()
    print(cls.main(rec_csv=True))