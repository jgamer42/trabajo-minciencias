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
from utils.escritor import escritor
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
        escritor("texto",item)