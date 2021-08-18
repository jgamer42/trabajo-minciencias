import os
os.chdir("/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red")
carpetas = os.listdir()
ignorados = ["pdfs_recortes","pdfs_particulares","videosAudiovisual","pdfs_originales","exports","completos"]
salida = {"totales":{},"caracteres":{},"palabras":{}}
for formato in carpetas:
    if formato in ignorados:
        continue
    else:
        salida[formato]={}
        medios = os.listdir(formato)
        for medio in medios:
            archivos = os.listdir(f"/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/{formato}/{medio}")
            salida[formato][medio] = len(archivos)
            try:
                salida["totales"][medio] += len(archivos)
            except:
                salida["totales"][medio] = len(archivos)
            for archivo in archivos:
                aux = open(f"/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/{formato}/{medio}/{archivo}")
                texto = aux.read()
                palabras = texto.split(" ")
                try:
                    salida["caracteres"][medio] += len(texto)
                except:
                    salida["caracteres"][medio] = len(texto)
                try:
                    salida["palabras"][medio] += len(palabras)
                except:
                    salida["palabras"][medio] = len(palabras)
for key in salida.keys():
    print(f"==={key}===")
    for universidad in salida[key].keys():
        print(f"{universidad}:{salida[key][universidad]}")