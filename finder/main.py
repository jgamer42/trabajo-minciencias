
import re
import unidecode
import pandas as pd

ruta_base ="/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/completos"
contexto = pd.read_csv("contexto_modificado.csv")
links = {}
palabras = contexto["palabra clave"]
corpus = contexto["corpus"]
universidad = contexto["universidad"]

for i,palabra in enumerate(palabras):
    aux = open(f"{ruta_base}/{corpus[i].strip()}_medio/{universidad[i].strip()}.txt","r")
    notas = aux.read().split("**** *AnalisisMediosUniversitarios")
    if palabra in links.keys():
        pass
    else:
        links[palabra] = [] 
    for nota in notas:
        if unidecode.unidecode(palabra.strip().lower()) in unidecode.unidecode(nota.lower().strip()):
            aux_nota = unidecode.unidecode(nota.lower().strip())
            regex = re.compile(r"http[s]?://([a-zA-z-?=./0-9]+)")
            a = regex.search(nota)
            links[palabra].append(a.group())

print(links)
#print(links)
for k in links.keys():
    print(k,len(links[k]))

