# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import site
site.addsitedir("../../../")
from utils.buscar_palabras import buscar_palabras
from utils import control_fechas
import os
class TextualPipeline:
    def process_item(self, item, spider):
        if item["fecha"] == "no disponible" or item["fecha"] == "no disponible en este medio" or item["fecha"] == None or item["fecha"] == [] :
            item["fecha"] = "00/00/0000"
        else:
            aux = control_fechas.valor(item["fecha"])
            item["fecha"] = f"{aux[0]}/{aux[1]}/{aux[2]}"
        if item["exploracion_general"]:
            self.validar_palabras_clave(item)
        else:
            self.procesar(item)
        return item

    def validar_palabras_clave(self,item):
        validar = buscar_palabras(item["contenido"])
        if validar[0] == True:
            item["etiqueta_exploracion"] = validar[1]
            self.procesar(item)

    def procesar(self,item):
        ruta = os.path.realpath(f"../../../corpus/red/texto/{item['medio']}/{item['titulo']}.txt")
        archivo = open(ruta,"w+")
        archivo.write(f"**** *AnalisisMediosUniversitarios\n")
        archivo.write(f"**** *TipoNoticias_Textuales *Medio_{item['nombre_medio']} *Ciudad_{item['ciudad']} *Departamento_{item['departamento']} *Fecha_{item['fecha']}")
        archivo.write(f"titulo: {item['titulo']}\n\n")
        archivo.write(f"medio: {item['medio']}\n\n")
        archivo.write(f"link: {item['link']}\n\n")
        archivo.write(f"fecha: {item['fecha']}\n\n")
        archivo.write(f"contenido principal: {item['contenido']}\n\n")
        archivo.write(f"contenido auxiliar: {item['contenido_auxiliar']}\n\n")
        archivo.write(f"etiqueta exploracion: {item['etiqueta_exploracion']}\n\n")
        archivo.write(f"ciudad: {item['ciudad']}\n\n")
        archivo.write(f"departamento: {item['departamento']}\n\n")
        archivo.write(f"nombre medio: {item['nombre_medio']}\n\n")
        archivo.write(f"universidad: {item['universidad']}\n\n")
        archivo.close()