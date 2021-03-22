import pandas as pd
from pagina import descargar
data = pd.read_csv("modelo.csv")
links = list(set(data["link"]))
nombres = list(set(data["nombre"]))
i = 0
print(links)
for link in links:
    descargar(link,nombres[i])
    i = i +1
