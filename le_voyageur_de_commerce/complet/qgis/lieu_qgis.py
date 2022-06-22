import pandas as pd
import numpy as np
import param

class Lieu_qgis:

    def __init__(self, path_csv=param.LIEUX_CSV_QGIS):
        self.df = pd.read_csv(path_csv)

    def main(self, rec_csv=False):
        x, y = [], []

        for i in self.df['latlong']:

            abs = i.split(',')[0]
            ord = i.split(',')[1]

            # abs = str(np.round(float(abs), 3)*1000)
            # ord = str(np.round(np.abs(float(ord)),3)*10000)
            
            
            # abs = int(abs[2:5])
            # ord = int(ord[2:5])

            x.append(abs)
            y.append(ord)


            data = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])

        if rec_csv == True:
            data.to_csv(param.LIEUX_CSV_QGIS_PROCESSED, index=False)

        return data

    

if __name__ == '__main__':
    cls = Lieu_qgis()
    print(cls.main(rec_csv=True))