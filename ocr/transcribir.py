import configparser
import os
import site
import pandas as pd
site.addsitedir("..")
from utils.escritor import  escritor
from ocr2 import ocr_space_file
data = pd.read_csv("modelo.csv")
fechas = data.fecha
nombres = data.nombre
universidad = data.universidad
links = data.link
i = 0
base = os.path.dirname(os.getcwd())


for nombre in nombres:
    #print(nombre,fechas[i],universidad[i],links[i])
    ruta = base+f"/corpus/periodicos/{universidad[i]}"
    if os.path.isdir(ruta):
        pass
    else:
        os.mkdir(ruta)
    i = i + 1