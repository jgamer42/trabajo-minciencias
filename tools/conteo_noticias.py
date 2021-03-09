import os 
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
carpetas = config["carpetas"]["carpetas"]
carpetas = carpetas.split(",")
os.chdir("../corpus/red/texto")
print("informe general")
total = 0
for carpeta in carpetas:
    archivos = os.listdir(carpeta)
    print(carpeta,len(archivos))
    total += len(archivos)
print("total: ",total)