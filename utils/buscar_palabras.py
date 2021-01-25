import configparser
def buscar_palabras(texto):
    config = configparser.ConfigParser()
    config.sections()
    bandera = False
    config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
    palabras = config["palabras"]["palabras"]
    palabras = palabras.split(",")
    etiqueta = None
    print(palabras)
    for palabra in palabras:
        busqueda = texto.find(palabra)
        print(palabra, busqueda)
        if busqueda >= 0:
            bandera = True
            etiqueta = palabra
            break
        else:
            pass
    return (bandera ,palabra)

