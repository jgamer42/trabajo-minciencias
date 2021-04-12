import os
def escritor(corpus,item):
    base = os.path.dirname(os.path.dirname(__file__))
    ruta = os.path.realpath(f"{base}/corpus/red/{corpus}/{item['carpeta']}/{item['titulo']}.txt")
    archivo = open(ruta,"w+")
    archivo.write(f"**** *AnalisisMediosUniversitarios\n")
    archivo.write(f"**** *TipoNoticias_{corpus} *Medio_{item['nombre_medio']} *Ciudad_{item['ciudad']} *Departamento_{item['departamento']} *Fecha_{item['fecha']}\n")
    if corpus == "texto":
        archivo.write(f"{item['titulo']}\n\n")
        archivo.write(f"{item['link']}\n\n")
        archivo.write(f"{item['fecha']}\n\n")
        archivo.write(f"{item['contenido']}\n\n")
        archivo.write(f"{item['contenido_auxiliar']}\n\n")
        archivo.write(f"{item['etiqueta_exploracion']}\n\n")
        archivo.write(f"{item['ciudad']}\n\n")
        archivo.write(f"{item['departamento']}\n\n")
        archivo.write(f"{item['nombre_medio']}\n\n")
        archivo.write(f"{item['universidad']}\n\n")

    elif corpus == "sonoro" or corpus == "periodico":
        archivo.write(f"{item['titulo']}\n\n")
        archivo.write(f"{item['link']}\n\n")
        archivo.write(f"{item['fecha']}\n\n")
        archivo.write(f"{item['contenido']}\n\n")
        archivo.write(f"{item['ciudad']}\n\n")
        archivo.write(f"{item['departamento']}\n\n")
        archivo.write(f"{item['nombre_medio']}\n\n")
        archivo.write(f"{item['universidad']}\n\n")
    archivo.close()