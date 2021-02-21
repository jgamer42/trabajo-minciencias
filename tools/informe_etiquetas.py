import os 
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
carpetas = config["carpetas"]["carpetas"]
carpetas = carpetas.split(",")
os.chdir("../corpus/red/texto")
print("informe general")
os.system("../../../tools/informe_etiquetas.sh")
for carpeta in carpetas:
    print("\n\n"+carpeta)
    os.chdir(f"./{carpeta}")
    os.system("../../../../tools/informe_etiquetas.sh")
    print("\ntotal noticias: ",end="")
    os.system("ls | wc -l")
    os.chdir("../")