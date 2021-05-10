import json
import os 
import site 
site.addsitedir("..")
from utils.reducir_dimension import reducir_dimension
base = "/home/jaime/cosas/codigo/trabajo-minciencias/"



def etiquetar(item,corpus):
    try:
        texto = item["contenido"] + item["contenido_auxiliar"]
    except:
        texto = item["contenido"]
    etiquetas = f'''"**** *AnalisisMediosUniversitarios"
**** *TipoNoticias_{corpus} *Universidad_{item['universidad']} *Medio_{item['nombre_medio']} *Ciudad_{item['ciudad']} *Departamento_{item['departamento']} *Fecha_{item['fecha']}
{item["titulo"]}
{item["link"]}
{texto}
"'''
    return etiquetas

def cargar_archivos_web():
    global base
    os.chdir(base+"corpus/red/exports")
    archivos_no_cargados = os.listdir()
    archivos_cargados = []
    for no_cargado in archivos_no_cargados:
        file = open(no_cargado)
        try:
            archivo_cargado = json.load(file)
            archivos_cargados.append(archivo_cargado)
        except:
            continue
    archivos = reducir_dimension(archivos_cargados)
    return archivos

def buscar_años_web(archivos):        
    os.chdir(base)
    fechas = []
    for archivo in archivos:
        año = archivo["fecha"].split("/")[-1]
        fechas.append(año)
    fechas = list(set(fechas))
    return fechas

def construir_relacion_fecha_texto(fechas,archivos):
    corpus = {}
    for fecha in fechas:
        corpus[fecha] = []
        for archivo in archivos:
            if archivo["fecha"].split("/")[-1] == fecha:
                corpus[fecha].append(archivo)
    return corpus

def escribir(corpus):
    global base
    os.chdir(base+"corpus/red/completos")
    for fecha in corpus.keys():
        elementos = corpus[fecha]
        for elemento in elementos:
            a = fecha.replace("/","-")
            texto = etiquetar(elemento,"textual")
            texto = texto.replace("\"","")
            texto = texto.replace("\'","")
            if "\'" in texto:
                os.system(f'echo "{texto}" >> "{a}".txt')
            else:
                os.system(f"echo '{texto}' >> '{a}'.txt")

def pipeline_web():
    archivos = cargar_archivos_web()
    años = buscar_años_web(archivos)
    corpus = construir_relacion_fecha_texto(años,archivos)
    escribir(corpus)

pipeline_web()
