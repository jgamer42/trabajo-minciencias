import pandas as pd
from pagina import descargar
data = pd.read_csv("primera extraccion.csv")
links = data.link.unique()
nombres = data.nombre.unique()
i = 0
for link in links:
    descargar(link,nombres[i])
    i = i +1
