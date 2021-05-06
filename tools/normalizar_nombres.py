import os
import re 
base = os.path.dirname(os.getcwd())
corpus = base+f"/corpus/red/pdfs_recortes"
os.chdir(corpus)
archivos = os.listdir()
regex = r"[a-z]+_\d+-[0-9]+"
for archivo in archivos:
    nombre = archivo.lower()
    nombre = nombre.strip()
    os.rename(archivo,nombre)
    if "Nº" in archivo:
        nombre_aux = nombre.replace("Nº","")
        try:
            os.rename(nombre,nombre_aux) 
        except:
            print(f"archivo repetido {nombre_aux}")
    elif "nº" in archivo:
        nombre_aux = nombre.replace("nº","")
        try:
            os.rename(nombre,nombre_aux) 
        except:
            print(f"archivo repetido {nombre_aux}")
    #print(archivo)
    if re.search(regex,archivo):
        aux = archivo.split("-")
        nombre = "[".join(a)
        aux = salida.split(".")
        salida = "].".join(a)
        try:
            os.rename(archivo,salida) 
        except:
            print(f"archivo repetido {nombre_aux}")
    if "edicion" in archivo:
        nombre = archivo.split("_")[1]
        aux = ["dateate",nombre]
        nombre = "_".join(aux)
        os.rename(archivo,nombre) 
    if "unpretexto" in archivo:
        nombre = archivo.replace("un","")
        os.rename(archivo,nombre) 
    nombre = nombre.strip()
    nombre = nombre.replace(",","-")
    os.rename(archivo,nombre)
    nombre = nombre.strip()
    os.rename(archivo,nombre)
    