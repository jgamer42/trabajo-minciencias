import os
def escritor(corpus,item):
    base = os.path.dirname(os.path.dirname(__file__))
    ruta = os.path.realpath(f"{base}/corpus/red/{corpus}/{item['carpeta']}/{item['titulo']}.txt")
    archivo = open(ruta,"w+")
    archivo.write(f"**** *AnalisisMediosUniversitarios\n")
    archivo.write(f"**** *TipoNoticias_Textuales *Medio_{item['nombre_medio']} *Ciudad_{item['ciudad']} *Departamento_{item['departamento']} *Fecha_{item['fecha']}")
    if corpus == "texto":
        archivo.write(f"titulo: {item['titulo']}\n\n")
        archivo.write(f"link: {item['link']}\n\n")
        archivo.write(f"fecha: {item['fecha']}\n\n")
        archivo.write(f"contenido principal: {item['contenido']}\n\n")
        archivo.write(f"contenido auxiliar: {item['contenido_auxiliar']}\n\n")
        archivo.write(f"etiqueta exploracion: {item['etiqueta_exploracion']}\n\n")
        archivo.write(f"ciudad: {item['ciudad']}\n\n")
        archivo.write(f"departamento: {item['departamento']}\n\n")
        archivo.write(f"nombre medio: {item['nombre_medio']}\n\n")
        archivo.write(f"universidad: {item['universidad']}\n\n")

    elif corpus == "sonoro":
        archivo.write(f"titulo: {item['titulo']}\n\n")
        archivo.write(f"link: {item['link']}\n\n")
        archivo.write(f"fecha: {item['fecha']}\n\n")
        archivo.write(f"contenido: {item['contenido']}\n\n")
        archivo.write(f"ciudad: {item['ciudad']}\n\n")
        archivo.write(f"departamento: {item['departamento']}\n\n")
        archivo.write(f"nombre medio: {item['nombre_medio']}\n\n")
        archivo.write(f"universidad: {item['universidad']}\n\n")
    archivo.close()