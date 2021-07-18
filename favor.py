from utils.extraer_audio import transcribir
import os
ruta = "/home/jaime/cosas/codigo/trabajo-minciencias/audiovisual/videos"
archivos = os.listdir(ruta)
for archivo in archivos:
    print(f"transcribiendo {archivo}")
    nombre = archivo.split(".")[0]
    os.system(f"ffmpeg -i '{ruta}/{archivo}' -vn '{ruta}/{nombre}.webm'")
    transcripcion = transcribir(f"{nombre}.webm")
    os.system(f"echo {transcripcion} >> {nombre}.txt")