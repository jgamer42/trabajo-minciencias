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
    archivo = open(f"../model/{universidad}.json")
    modelo = json.load(archivo)
    modelo["titulo"] = nombre
    modelo["fecha"] = fecha
    modelo["link"] = link
    archivo = destino.split("/")[-1]
    archivo = archivo.split(".")[0]
    archivo = archivo+".txt"
    if  os.path.isfile(f"/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/periodicos/{modelo['carpeta']}/{archivo}"):
        pass     
    else:
        print(f"no esta: {modelo['carpeta']}/{archivo}")
        texto = ocr_space_file(destino)
        if texto == None:
            print("fallo la transcripcion\n")
        else:
            print("transcripcion exitosa\n")
            modelo["contenido"] = texto
            escritor("periodicos",modelo)


data = pd.read_csv("modelo.csv")
fechas = data.fecha
nombres = data.nombre
universidad = data.universidad
paginas = data.paginas
links = data.link
i = 0
base = os.path.dirname(os.getcwd())
corpus = base+"/corpus/red/pdfs_recortes"
for nombre in nombres:
    archivo = f"/{nombre}[{paginas[i]}].pdf"
    destino = corpus + archivo
    if not(os.path.isfile(destino)):
        print(f"no encontro {archivo} \n")
    else:
        if ("plataforma_35" in archivo) or ("periódico15_345" in archivo) or ("plataforma_17" in archivo) or ("plataforma_18" in archivo) or ("plataforma_23" in archivo) or ("plataforma_24" in archivo) or ("plataforma_25" in archivo) or ("plataforma_29" in archivo) or ("plataforma_31" in archivo) or ("plataforma_38" in archivo) or ("plataforma_40" in archivo) or ("pretexto_2" in archivo) or ("pretexto_4" in archivo) or ("pretexto_6" in archivo) or ("pretexto_7" in archivo) or ("pretexto_8" in archivo) or ("urbe_61" in archivo) or ("urbe_82" in archivo) or ("urbe_84" in archivo) or ("urbe_93" in archivo) or ("urbe_96" in archivo):
            pass
        else:
            escribir_txt(destino,universidad[i],links[i],f"{nombre}[{paginas[i]}]",fechas[i])
    i = i + 1
#print(os.path.isfile(f"/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/periodicos/udea/urbe_43[10].txt"))
