import os 
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("general.cfg")
universidades = config["carpetas"]["carpetas"]
universidades = universidades.split(",") 
os.chdir("web_scrapping/red/textual/textual")
for universidad in universidades:
    print(universidad,"\n\n\n")
    os.system(f"scrapy crawl {universidad} -O ../../../../corpus/red/exports/{universidad}.json")
