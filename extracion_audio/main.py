import pandas as pd 
from descargas import descargar
import os
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
while i < len(universidades):
    descargar(links[i],universidades[i])
    ruta = f"{ruta}/{universidades[i]}"
    aux_archivos = glob.glob(f"{ruta}/*")
    archivo = max(aux_archivos,key=os.path.getctime)
    archivo = archivo.split("/")[-1]
    origen = f"{ruta}/{archivo}"
    destino = f"{ruta}/{universidades[i]}_{i}.webm" 
    os.system(f"ffmpeg -i '{origen}' -vn '{destino}'")
    transcripcion = transcribir(destino)
    modelo = open(f"{base}model/{universidades[i].strip()}.json")
    model = json.load(archivo)
    model["titulo"] = archivo
    model["link"] = links[i]
    model["fecha"] = fechas[i]
    model["contenido"] = transcripcion
    escritor("sonoro",model)   
    i += 1