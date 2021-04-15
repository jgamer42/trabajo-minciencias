import configparser
import os
import site
import pandas as pd
site.addsitedir("..")
from utils.escritor import  escritor
from ocr2 import ocr_space_file
import json
import time

def escribir_txt(destino,universidad,link,nombre,fecha):
    texto = ocr_space_file(destino)
    archivo = open(f"../model/{universidad}.json")
    modelo = json.load(archivo)
    modelo["titulo"] = nombre
    modelo["contenido"] = texto
    modelo["fecha"] = fecha
    modelo["link"] = link
    escritor("periodico",modelo)            
        

data = pd.read_csv("modelo.csv")
fechas = data.fecha
nombres = data.nombre
universidad = data.universidad
paginas = data.paginas
links = data.link
i = 0
base = os.path.dirname(os.getcwd())
corpus = base+"/corpus/red/pdfs_recortes_completos"

for nombre in nombres:
    archivo = f"/{universidad[i]}/{nombre}[{paginas[i]}].pdf"

    destino = corpus + archivo
    if not(os.path.isfile(destino)):
        print(f"no encontro {archivo}")
    else:
        try:
            escribir_txt(destino,universidad[i],links[i],f"{nombre}[{paginas[i]}]",fechas[i])
        except:
            print(f"excede el tamaño {nombre}[{paginas[i]}].pdf")
    i = i + 1

    