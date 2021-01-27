import re 
def valor(texto):
    if texto == None or texto == "no disponible en este medio":
        return 0
    else:
        return identificar_formato(texto)

def identificar_formato(texto):
    identificador = texto[-4:]
    identificador_2 = texto.split(",")
    if len(identificador_2) == 2:
        return formato_5(texto)
    elif re.search("^[0-9]{2}",texto):
        return formato_4(texto)
    elif "de" in texto:
        return formato_2(texto)
    elif re.search("[0-9]{4}",identificador):
        return formato_1(texto)
    elif re.search(":[0-9]{2}",identificador):
        return formato_3(texto)
    else:
        print("es otro formato")
        return 0


#funcion encargada de procesar las fechas en formato "Jueves, Abril 24, 2014"
#formato usado en tadeo
def formato_1(texto):
    data = texto.split(",")[1:]
    año = data[1].strip()
    aux = data[0].split(" ")
    dia = aux[2]
    mes = identificar_mes(aux[1])
    fecha = [int(dia),mes,int(año)]
    return fecha

#funcion encargada de procesar las fechas en formato "Jueves 20 de Febrero 2014"
#formato usado en tadeo
def formato_2(texto):
    data = texto.split(" ")
    mes = identificar_mes(data[3])
    return [int(data[1]),mes,int(data[4])]

#funcion encargada de procesar las fechas en formato "Jueves, Febrero 14, 2019 - 15:00"
#formato usado en tadeo
def formato_3(texto):
    texto = texto.split(",")[1:]
    aux = texto[1].split("-")
    año = aux[0].strip()
    aux = texto[0].split(" ")
    mes = aux[1].strip()
    mes = identificar_mes(mes)
    dia = aux[2].strip()
    return [int(dia),mes,int(año)]

#funcion encargada de procesar las fechas en formato "08 de Abril de 2020"
#formato usado en tadeo
def formato_4(texto):
    texto = texto.split(" ")
    mes = identificar_mes(texto[2])
    return [int(texto[0]),mes,int(texto[-1])]

#funcion encargada de procesar las fechas en formado "octubre 30, 2020"
#formato usado en Eafit
def formato_5(texto):
    data = texto.split(",")
    año = int(data[-1].strip())
    aux = data[0].split(" ")
    mes = identificar_mes(aux[0].strip())
    dia = int(aux[1].strip())
    return [dia,mes,año]


def identificar_mes(texto):
    texto = texto.lower()
    año={
        "enero":1,
        "febrero":2,
        "marzo":3,
        "abril":4,
        "mayo":5,
        "junio":6,
        "julio":7,
        "agosto":8,
        "septiembre":9,
        "octubre": 10,     
        "noviembre":11,
        "diciembre":12
    }
    salida = None
    for mes in año.keys():
        if texto == mes:
            salida = año[mes]
    return salida

