import pandas as pd 
import descargas
import os
data = pd.read_csv("modelo.csv")
links = data["Link"]
universidades = data["Medio"]

i = 0
base = os.getcwd()
while i < len(universidades):
    #if universidades[i] == "UNIMINUTO RADIO":
    #    descargas.uniminutoradio(links[i])
    if "ivoox" in links[i]:
        print(universidades[i])
        print(links[i])
        descargas.ivoox(links[i],universidades[i])
    else:
        pass
    os.chdir(base)
    i += 1