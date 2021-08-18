import os 
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("../general.cfg")
#universidades = config["carpetas"]["carpetas"]
#universidades = universidades.split(",") 
corpus = "sonoro"
universidades = ["bolivarianaBucaramanga","bolivarianaMedellin","fundacionUniversitariaPopayan","udea","uniminutoradio","universidadManizales","universidadIbague"]
#universidades = ["eafit","politecnico","santiagoCali","udea","unisabana","univalle","universidadIbague"]
#universidades = ["autonomaBucaramanga","bolivarianaBucaramanga","bolivarianaMedellin","luisAmigo","santiagoCali","udea","uniminutoMedellin","uniminutoradio","universidadBoyaca"]
base = os.path.dirname(os.getcwd())
for universidad in universidades:
    os.chdir(base+f"/corpus/red/{corpus}/{universidad}")
    nombre = ""
    if "eafit" in universidad:
        nombre = "eafit"
    elif "plataforma" in universidad:
        nombre = "plataforma"
    elif "periodico15_conflicto" == universidad:
        nombre = "autonomaBucaramanga"
    else:
        nombre = universidad
    archivos = os.listdir()
    os.chdir(base)
    print(universidad)
    #print(archivos,"\n\n")
    for archivo in archivos:
        ruta = base+f"/corpus/red/{corpus}/{universidad}/{archivo}"
        print(ruta)
        if "\'" in ruta:
            os.system(f'cat "{ruta}" >> {base}/corpus/red/completos/{nombre}.txt')
        else:
            os.system(f"cat '{ruta}' >> {base}/corpus/red/completos/{nombre}.txt")