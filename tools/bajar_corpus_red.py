import os 
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
carpetas = config["carpetas"]["carpetas"]
carpetas = carpetas.split(",")
os.chdir("../web_scrapping/red/textual")
for carpeta in carpetas:
    os.system(f"scrapy crawl {carpeta} -O /home/jaime/compartida/codigo/trabajo-minciencias/corpus/red/exports/{carpeta}.json")