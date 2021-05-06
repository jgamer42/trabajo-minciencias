import os 
base = os.path.dirname(os.getcwd())
destino = "completos"
corpus = base +f"/corpus/red/{destino}"
os.chdir(corpus)
carpetas = os.listdir()
for carpeta in carpetas:
    os.chdir(carpeta)
    archivos = os.listdir()
    for archivo in archivos:
        os.remove(archivo)
    os.chdir(corpus)