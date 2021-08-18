from sys import exc_info
import pandas as pd 
from descargas import descargar
import os
import logging
import site
import glob
import json
site.addsitedir("/home/jaime/cosas/codigo/trabajo-minciencias/")
from utils.extraer_audio import transcribir
from utils.escritor import escritor
data = pd.read_csv("modelo.csv")
links = data["Link"]
universidades = data["Universidad"]
fechas = data["Fecha"]
base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
ruta = "/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/sonoro"
i = 0

logging.basicConfig(filename="errors.log",filemode='w',)
while i < len(universidades):
    destino = ""
    archivo = ""
    #if universidades[i] != "uniminutoradio":
    descargar(links[i],universidades[i])
    aux_ruta = f"{ruta}/{universidades[i]}"
    try:
        aux_archivos = glob.glob(f"{aux_ruta}/*")
        archivo = max(aux_archivos,key=os.path.getctime)
        archivo = archivo.split("/")[-1]
        origen = f"{aux_ruta}/{archivo}"
        destino = f"{aux_ruta}/{universidades[i]}_{i}.webm" 
        print(destino)
        os.system(f"ffmpeg -i '{origen}' -vn '{destino}'")
    except:
        logging.warning(f"fallo en la descarga o conversion del archivo link:{links[i]}\n",exc_info=True)
    try:
        print(destino)
        print("transcribiendo")
        transcripcion = transcribir(destino)
        print(transcripcion)
    except:
        logging.warning(f"fallo en opteniendo la transcripcio link:{links[i]}\n",exc_info=True)
    try:
        puntero_json = open(f"{base}model/{universidades[i].strip()}.json")                
        model = json.load(puntero_json)
        model["titulo"] = archivo
        model["link"] = links[i]
        model["fecha"] = fechas[i]
        model["contenido"] = transcripcion
    except:
        logging.warning(f"fallo en abriendo el json link:{links[i]}\n",exc_info=True)
    try:
        escritor("sonoro",model)    
    except:
        logging.warning(f"fallo en la linea 37 modelo:{model}\nlink:{links[i]}\n",exc_info=True)
    i += 1
        