import os 
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("../general.cfg")
universidades = config["carpetas"]["carpetas"]
universidades = universidades.split(",") 
base = os.path.dirname(os.getcwd())
os.chdir(base+"/corpus/red/texto")
for universidad in universidades:
    os.mkdir(universidad)