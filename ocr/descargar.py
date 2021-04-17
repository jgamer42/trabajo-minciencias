import pandas as pd
from pagina import descargar
import time
import os
data = pd.read_csv("modelo.csv")
links = data.link
nombres = data.nombre

print(data.columns)

i = 0
base = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.realpath(f"{base}/pdfs/")
os.chdir(ruta)
for link in links:
    if f"{nombres[i]}.pdf" in os.listdir():
        print(f"{nombres[i]} estaba")
    elif not("plataforma" in nombres[i]):
        descargar(link,nombres[i])
        print(f"{nombres[i]} descargando")
        time.sleep(3)
    elif "plataforma" in nombres[i]:
         os.system(f"wget -O{nombre}.pdf {links[i]}")  
    i = i + 1


    



