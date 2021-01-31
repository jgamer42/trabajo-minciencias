import configparser 
import os 
config = configparser.ConfigParser()
config.sections()
config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
carpetas = config["carpetas"]["carpetas"]
carpetas = carpetas.split(",")
os.chdir("../")
for carpeta in carpetas:
    os.system(f"scrapy crawl {carpeta} -o exports/{carpeta}.json")