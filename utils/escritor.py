import os
import configparser
def escritor(corpus,item):
    base = os.path.dirname(os.path.dirname(__file__))
    ruta = os.path.realpath(f"{base}/corpus/red/{corpus}/{item['carpeta']}/{item['titulo']}.txt")
    config = configparser.ConfigParser()
    config.sections()
    #config.read("../../../general.cfg")
    config.read("../general.cfg")
    baneadas = config["palabras_clave"]["bloqueadas"]

    baneadas = baneadas.split(",") 
    bandera = False
    for baneada in baneadas:
        try:
            if baneada in item["contenido"] or baneada in item["contenido_auxiliar"]:
                bandera = True
                break
        except:
            if baneada in item["contenido"]:
                bandera = True
                break
    if not(bandera):
        cadena(ruta,item,corpus)

def cadena(ruta,item,corpus):
    etiquetas1 = f"**** *AnalisisMediosUniversitarios"
    etiquetas2 = f"**** *TipoNoticias_{corpus} *Universidad_{item['universidad']} *Medio_{item['nombre_medio']} *Ciudad_{item['ciudad']} *Departamento_{item['departamento']} *Fecha_{item['fecha']}"
    texto = item["contenido"].replace("\"","")
    texto = item["contenido"].replace("\'","")
    if "\'" in ruta:
        os.system(f'echo "{etiquetas1}" >> "{ruta}"')
        os.system(f'echo "{etiquetas2}" >> "{ruta}"')
        os.system(f'echo "{item["titulo"]}" >> "{ruta}"')
        os.system(f'echo "{item["link"]}" >> "{ruta}"')
        os.system(f'echo "{texto}" >> "{ruta}"')
        try:
            os.system(f'echo "{item["contenido_auxiliar"]}" >> "{ruta}"')
        except:
            pass
    else:
        os.system(f"echo '{etiquetas1}' >> '{ruta}'")
        os.system(f"echo '{etiquetas2}' >> '{ruta}'")
        os.system(f"echo '{item['titulo']}' >> '{ruta}'")
        os.system(f"echo '{item['link']}' >> '{ruta}'")
        os.system(f"echo '{texto}' >> '{ruta}'")
        try:
            os.system(f"echo '{item['contenido_auxiliar']}' >> '{ruta}'")
        except:
            pass
