import streamlit as st
import pandas as pd
import numpy as np

lat = [47.3306, 47.3144, 47.3654, 47.3674]
lon = [-3.1885, -3.1917, -3.22577, -3.22434]
etoiles = ['2**', '2**', "","2**"]
name = ['trion guen', 'camping municipal Bangor', 'la source', 'camping municipal pen prat']


data = pd.DataFrame(list(zip(lat, lon, etoiles)), columns = ['lat', 'lon', 'étoiles'], index=name)


# st.title('Les campings vus par Chloé')

# st.map(data)

# st.write(data.head())

import folium
c= folium.Map(location=[47.33757333979535, -3.199220649812984], zoom_start=12)

for i in range(len(lat)):
    texte = name[i] + ' \n '+  etoiles[i]
    folium.Marker([lat[i], lon[i]], popup=texte).add_to(c)


c.save('maCarte.html')