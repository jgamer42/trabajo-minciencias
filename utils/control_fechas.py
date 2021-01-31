import re 
def valor(texto):
    if (texto == None) or (texto == "no disponible en este medio") or (texto == "no diponible"):
        return 0
    else:
        return identificar_formato(texto)

def identificar_formato(texto):
    identificador = texto[-4:]
    identificador_2 = texto.split(",")
    if len(identificador_2) == 2:
        if re.search("^[0-9]",texto):
            return formato_6(texto)
        elif re.search(":[0-9]{2}",identificador):
            return formato_9(texto)
        else:
            return formato_5(texto)
    elif re.search("^[0-9]{2}",texto):
        if "de" in texto:
            return formato_4(texto)
        elif "-" in texto:
            return formato_10(texto)
        else:
            return formato_8(texto)
    elif "de" in texto:
        return formato_2(texto)
    elif re.search("[0-9]{4}",identificador):
        if len(texto.split(" ")) == 3:
            return formato_8(texto)
        else:
            return formato_1(texto)
    elif re.search(":[0-9]{2}",identificador):
        return formato_3(texto)
    elif "Creado" in texto:
        return formato_7(texto)
    else:
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
#formato usado en tadeo , autonoma bucaramanga(periodico 15)
def formato_4(texto):
    texto = texto.split(" ")
    mes = identificar_mes(texto[2])
    return [int(texto[0]),mes,int(texto[-1])]

#funcion encargada de procesar las fechas en formato "octubre 30, 2020"
#formato usado en Eafit
def formato_5(texto):
    data = texto.split(",")
    año = int(data[-1].strip())
    aux = data[0].split(" ")
    mes = identificar_mes(aux[0].strip())
    dia = int(aux[1].strip())
    return [dia,mes,año]

#funcion encargada de procesar en formato "27 septiembre, 2018"
#formato usado en uniminuto radio
def formato_6(texto):
    data = texto.split(",")
    año = int(data[-1].strip())
    aux = data[0].split()
    mes = identificar_mes(aux[-1])
    dia = int(aux[0].strip())
    return [dia,mes,año]

#funcion encargada de procesar el formato "Creado el 07 Febrero 2020"
#formato usado bolivariana bucaramanga
def formato_7(texto):
    data = texto.split(" ")
    dia = int(data[2])
    año = int(data[4][:-1])
    mes = identificar_mes(data[3])
    return [dia,mes,año]

#funcion encargada de procesar el formato "22 Abril 2020"
#formato usado upb 
def formato_8(texto):
    data = texto.split(" ")
    dia = int(data[0])
    mes = identificar_mes(data[1].lower())
    año = int(data[2])
    return [dia,mes,año]

#funcion encargada de procesar el formato "Martes, 28 Enero 2020 18:17"
#formato usado por upb archivo noticias
def formato_9(texto):
    data = texto.split(",")
    data = data[1].split(" ")
    año = int(data[3])
    dia = int(data[1])
    mes = identificar_mes(data[2].lower())
    return [dia,mes,año]
#funcion encargada de procesar el formato "2016-06-20"
#formato usado por universidad de ibague
def formato_10(texto):
    data = texto.split("-")
    dia = int(data[-1])
    año = int(data[0])
    mes = int(data[1])
    return [dia , mes ,año]

def identificar_mes(texto):
    texto = texto.lower()
    if texto =="enero" or texto == "january":
        return 1
    elif texto =="febrero" or texto == "february":
        return 2
    elif texto == "marzo" or texto == "march":
        return 3
    elif texto == "abril" or texto == "april":
        return 4
    elif texto == "mayo" or texto == "may":
        return 5
    elif texto == "junio" or texto == "june":
        return 6
    elif texto == "julio" or texto == "july":
        return 7
    elif texto == "agosto" or texto == "august":
        return 8
    elif texto == "septiembre" or texto == "september":
        return 9
    elif texto == "octubre" or texto == "october":
        return 10     
    elif texto == "noviembre" or texto == "november":
        return 11
    elif texto == "diciembre" or texto == "december":
        return 12
    else:
        return None

