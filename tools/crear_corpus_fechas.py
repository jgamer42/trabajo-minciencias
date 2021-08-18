import os
import re 
base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
#universidades = ["autonomaBucaramanga","bolivarianaBucaramanga","bolivarianaMedellin","luisAmigo","santiagoCali","udea","uniminutoMedellin","uniminutoradio","universidadBoyaca"]
carpeta="sonoro"
#universidades = ["eafit","politecnico","santiagoCali","udea","univalle","universidadIbague","unisabana"]
universidades = ["bolivarianaBucaramanga","bolivarianaMedellin","fundacionUniversitariaPopayan","udea","uniminutoradio","universidadManizales","universidadIbague"]
def buscar_fecha_periodicos(texto):
    fecha = re.findall(r"[0-9]{2}\/[0-9]{2}\/[0-9]{2}",texto)
    if fecha == []:
        return "0000"
    else:
        año = fecha[0].split("/")[-1]
        return "20"+año

def buscar_fecha_audiovisual(texto):
    fecha = re.findall(r"Fecha_[0-9]{2}\/[0-9]{2}\/[0-9]{4}",texto)
    if fecha == []:
        return "0000"
    else:
        año = fecha[0].split("/")[-1]
        return año

def buscar_fecha(texto):
    global carpeta
    if carpeta == "periodicos":
        return buscar_fecha_periodicos(texto)
    else:
        return buscar_fecha_audiovisual(texto)
    

def generar_fechas():
    global base
    global universidades
    global carpeta
    fechas = []
    for universidad in universidades:
        os.chdir(base+f"corpus/red/{carpeta}/{universidad}")
        textos = os.listdir()
        for texto in textos:
            with open(base+f"corpus/red/{carpeta}/{universidad}/{texto}") as file:
                contenido = file.read()
                fechas.append(buscar_fecha(contenido))
            file.close()
    os.chdir(base)
    return list(set(fechas))

def generar_corpus(fechas):
    global base
    global universidades
    global carpeta
    salida = {}
    for universidad in universidades:
        for fecha in fechas:
            if fecha in salida.keys():
                pass
            else:
                salida[fecha] = []
            os.chdir(base+f"corpus/red/{carpeta}/{universidad}")
            textos = os.listdir()
            for texto in textos:
                with open(base+f"corpus/red/{carpeta}/{universidad}/{texto}") as file:
                    contenido = file.read()
                    if buscar_fecha(contenido) == fecha:
                        salida[fecha].append(texto)
                file.close()
    os.chdir(base)
    return salida

def generar_txt(corpus):
    global base
    global universidades
    global carpeta
    for llave in corpus.keys():
        for texto in corpus[llave]:
            ruta = ""
            for universidad in universidades:
                ruta = base+f"/corpus/red/{carpeta}/{universidad}/{texto}"
                if os.path.isfile(ruta):
                    if "\"" in ruta:
                        os.system(f"cat '{ruta}' >> {base}/corpus/red/completos/{llave}.txt")
                    else:
                        os.system(f'cat "{ruta}" >> {base}/corpus/red/completos/{llave}.txt')


fechas = generar_fechas()
corpus = generar_corpus(fechas)
generar_txt(corpus)
print(corpus)

    

