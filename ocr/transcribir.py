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
    archivo = open(f"/home/jaime/cosas/codigo/trabajo-minciencias/model/{universidad}.json")
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

def escribir_txt_particular(universidad,link,nombre,fecha):
    archivo = open(f"/home/jaime/cosas/codigo/trabajo-minciencias/model/{universidad}.json")
    modelo = json.load(archivo)
    modelo["titulo"] = nombre
    modelo["fecha"] = fecha
    modelo["link"] = link
    archivo = destino.split("/")[-1]
    archivo = archivo.split(".")[0]
    archivo = archivo+".txt"
    elementos_recortar = os.listdir("/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/pdfs_particulares")
    filtrados = filter(lambda elemento: nombre in elemento,elementos_recortar)
    if  os.path.isfile(f"/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/periodicos/{modelo['carpeta']}/{modelo['titulo']}"):
        pass
    else:
        print(f"no esta: {modelo['carpeta']}/{archivo}")
        texto = ""
        for dato in filtrados:
            texto = texto + ocr_space_file(f"/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/pdfs_particulares/{dato}")
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
        print(f"no encontro {archivo}")
    else:
        if archivo.split("/")[1] in ['plataforma_24[14-18].pdf', 'plataforma_29[27-30].pdf', 'pretexto_2[48-51].pdf', 'pretexto_4[28-35].pdf', 'plataforma_31[12-16].pdf', 'periódico15_345[6-9].pdf', 'plataforma_31[8-11].pdf', 'plataforma_18[14-18].pdf', 'plataforma_23[4-7].pdf', 'plataforma_38[38-41].pdf', 'plataforma_35[17-34].pdf', 'urbe_96[16-19].pdf', 'urbe_61[8-11].pdf', 'plataforma_23[8-13].pdf', 'urbe_82[15-32].pdf', 'plataforma_40[2-6].pdf', 'plataforma_25[34-37].pdf', 'plataforma_17[10-13].pdf', 'pretexto_7[47-53].pdf', 'urbe_93[2-5].pdf', 'pretexto_6[21-27].pdf', 'urbe_84[6-11].pdf', 'pretexto_8[65-69].pdf']:
            archivos = base + "/corpus/red/pdfs_particulares"
            escribir_txt_particular(universidad[i],links[i],nombre,fechas[i])
        else:
            escribir_txt(destino,universidad[i],links[i],f"{nombre}[{paginas[i]}]",fechas[i])
    i = i + 1