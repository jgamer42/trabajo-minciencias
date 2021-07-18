from numpy.lib.utils import source
import pandas as pd 
import site
import os
site.addsitedir("/home/jaime/cosas/codigo/trabajo-minciencias/")
from utils.extraer_audio import transcribir
from utils.escritor import escritor
from audiovisual.bajar import bajar
import json
SOURCE = pd.read_csv("extraible.csv")
i = 0
base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
links = SOURCE.link
dates = SOURCE.fecha
universidades = SOURCE.universidad
for link in links:
    archivo = open(f"{base}model/{universidades[i].strip()}.json")
    
    model = json.load(archivo)
    aux = bajar(link)
    if aux == None:
        pass
    else:
        model["titulo"] = aux
        model["link"] = link
        model["fecha"] = dates[i]
        aux = aux.replace(".","")
        aux = aux.replace(",","")
        aux = aux.replace(":","")
        aux = aux.replace("\"","")
        aux = aux.replace("\'","")
        try:
            model["contenido"] = transcribir(f"{aux}.webm")
            escritor("audiovisual",model)   
        except:
            print(f"{aux}.webm")
    i = i +1

