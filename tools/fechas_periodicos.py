import os
import re 
base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
universidades = ["autonomaBucaramanga","bolivarianaBucaramanga","bolivarianaMedellin","luisAmigo","santiagoCali","udea","uniminutoMedellin","uniminutoradio","universidadBoyaca"]
def buscar_fecha(texto):
    fecha = re.findall(r"[0-9]{2}\/[0-9]{2}\/[0-9]{2}",texto)
    if fecha == []:
        return "0000"
    else:
        año = fecha[0].split("/")[-1]
        return "20"+año

def generar_fechas():
    global base
    global universidades
    fechas = []
    for universidad in universidades:
        os.chdir(base+f"corpus/red/periodicos/{universidad}")
        textos = os.listdir()
        for texto in textos:
            with open(base+f"corpus/red/periodicos/{universidad}/{texto}") as file:
                contenido = file.read()
                fechas.append(buscar_fecha(contenido))
            file.close()
    os.chdir(base)
    return list(set(fechas))

def generar_corpus(fechas):
    global base
    global universidades
    salida = {}
    for universidad in universidades:
        for fecha in fechas:
            if fecha in salida.keys():
                pass
            else:
                salida[fecha] = []
            os.chdir(base+f"corpus/red/periodicos/{universidad}")
            textos = os.listdir()
            for texto in textos:
                with open(base+f"corpus/red/periodicos/{universidad}/{texto}") as file:
                    contenido = file.read()
                    if buscar_fecha(contenido) == fecha:
                        salida[fecha].append(texto)
                file.close()
    os.chdir(base)
    return salida

def generar_txt(corpus):
    global base
    global universidades
    for llave in corpus.keys():
        for texto in corpus[llave]:
            ruta = ""
            for universidad in universidades:
                ruta = base+f"/corpus/red/periodicos/{universidad}/{texto}"
                if os.path.isfile(ruta):
                    os.system(f"cat {ruta} >> {base}/corpus/red/completos/{llave}.txt")
            


fechas = generar_fechas()
corpus = generar_corpus(fechas)
generar_txt(corpus)
print(corpus)

    

