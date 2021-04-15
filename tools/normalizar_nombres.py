import os 
base = os.path.dirname(os.getcwd())
universidad = "bolivarianaBucaramanga"
corpus = base+f"/corpus/red/pdfs_recortes_completos/{universidad}"
os.chdir(corpus)
archivos = os.listdir()
for archivo in archivos:
    nombre = archivo.lower()
    print(archivo,nombre)
    os.rename(archivo,nombre)