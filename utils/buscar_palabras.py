import configparser
def buscar_palabras(texto):
    config = configparser.ConfigParser()
    config.sections()
    bandera = False
    #revisar aqui
    config.read("/home/jaime/cosas/codigo/trabajo-minciencias/general.cfg")
    palabras = config["palabras_clave"]["palabras"]
    palabras = palabras.split(",")
    etiqueta = None
    for palabra in palabras:
        busqueda = texto.find(palabra)
        if busqueda >= 0:
            bandera = True
            etiqueta = palabra
            break
        else:
            pass
    return (bandera ,palabra)

