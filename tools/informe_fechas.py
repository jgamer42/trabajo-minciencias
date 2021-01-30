import json
import site
from datetime import datetime
site.addsitedir("/home/jaime/compartida/codigo/trabajo-minciencias/utils")
import control_fechas 
#file = open("../exports/tadeo.json")
#file = open("../exports/eafit.json")
file = open("../exports/uniminutoradio.json")
raw_data = json.load(file)
fechas = []
for data in raw_data:
    print(data["fecha"])
    if data["fecha"] != None:
        fecha = control_fechas.valor(data["fecha"].strip())
        if fecha != 0:
            fecha = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
            fechas.append(fecha)
ordenadas = fechas.sort(key= lambda date:datetime.strptime(date,'%d/%m/%Y'))
print(fechas)


