import json
import site
from datetime import datetime
site.addsitedir("/home/jaime/compartida/codigo/trabajo-minciencias/utils")
import control_fechas
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
carpetas = config["carpetas"]["carpetas"]
carpetas = carpetas.split(",") 
for carpeta in carpetas:
    print(f"\n\n{carpeta}")
    file = open(f"../corpus/red/exports/{carpeta}.json")
    raw_data = json.load(file)
    fechas = []
    if "no dis" in raw_data[0]["fecha"]:
        print("no disponible")
        file.close()
    else:
        for data in raw_data:
            if data["medio"] == "bolivarianaMedellin":
                fecha = data["fecha"]
                if "-" in fecha:
                    pass
                elif "/" in fecha:
                    fecha = list(map(int,fecha.split("/")))
                    fecha = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
                    fechas.append(fecha)
            elif data["fecha"] != None:
                fecha = control_fechas.valor(data["fecha"].strip())
                if fecha != 0:
                    fecha = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
                    fechas.append(fecha)
        fechas.sort(key = lambda date:datetime.strptime(date,'%d/%m/%Y'))
        print(fechas[0],"-",fechas[-1])
        file.close()


    
       




