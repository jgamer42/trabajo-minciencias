# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import site
site.addsitedir("../../../")
from utils.buscar_palabras import buscar_palabras

class TextualPipeline:
    def process_item(self, item, spider):
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
        archivo = open(f"/home/jaime/compartida/codigo/trabajo-minciencias/corpus/red/texto/{item['medio']}/{item['titulo']}.txt","w+")
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