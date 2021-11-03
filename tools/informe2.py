import os 
ruta = "/home/jaime/cosas/codigo/trabajo-minciencias/drive"
carpetas = os.listdir(ruta)
data = {"totales":{}}
for corpus in carpetas:
    data["totales"][corpus]={}
    data["totales"][corpus]={}
    data["totales"][corpus]={}
    data["totales"][corpus]={}
    data[corpus]={}
    if "Análisis Corpus Gráfico (Fotografías)" != corpus:
        ruta2 = f"{ruta}/{corpus}"
        variables = os.listdir(ruta2)
        for variable in variables:
            ruta3 = f"{ruta2}/{variable}"
            aux = os.listdir(ruta3)[0]
            ruta4 = f"{ruta3}/{aux}"
            medios = os.listdir(ruta4)
            medios = [medio for medio in medios if not ".txt" in medio]
            data[corpus][variable] = {}
            for medio in medios:
                ruta5 = f"{ruta4}/{medio}"
                carpetas = os.listdir(ruta5)
                carpeta = [c for c in carpetas if "_stat_" in c]
                if len(carpeta) > 0:
                    carpeta=carpeta[0]
                    archivo = open(f"{ruta5}/{carpeta}/glob.txt").read()
                    converter = archivo.split("\n")[1:-1]
                    textos = int(converter[0].split(":")[1])
                    ocurrencias = int(converter[1].split(":")[1])
                    formas = int(converter[2].split(":")[1])
                    hapax = int(converter[3].split(":")[1].split("(")[0])
                    try:
                        data["totales"][corpus]["textos"] +=  textos
                    except:
                        data["totales"][corpus]["textos"] = textos
                    try:
                        data["totales"][corpus]["ocurrencias"] +=  ocurrencias
                    except:
                        data["totales"][corpus]["ocurrencias"] =  ocurrencias
                    try:
                        data["totales"][corpus]["formas"] +=  formas
                    except:
                        data["totales"][corpus]["formas"] =  formas
                    try:
                        data["totales"][corpus]["hapax"] +=  hapax
                    except:
                        data["totales"][corpus]["hapax"] =  hapax
                    

                    try:
                        data[corpus][variable]["textos"] +=  textos
                    except:
                        data[corpus][variable]["textos"] = textos
                    try:
                        data[corpus][variable]["ocurrencias"] +=  ocurrencias
                    except:
                        data[corpus][variable]["ocurrencias"] =  ocurrencias
                    try:
                        data[corpus][variable]["formas"] +=  formas
                    except:
                        data[corpus][variable]["formas"] =  formas
                    try:
                        data[corpus][variable]["hapax"] +=  hapax
                    except:
                        data[corpus][variable]["hapax"] =  hapax
                else:
                    pass
    else:
        continue

for key in data.keys():
    print(f"========={key}=======")
    if len(data[key].keys())>0:
        for llave in data[key].keys():
            if len(data[key][llave].keys()) > 0:
                print(f"{llave} : {data[key][llave]}")