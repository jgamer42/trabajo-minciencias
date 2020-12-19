# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EjemploPipeline:
    def process_item(self, item, spider):
        archivo = open(f"/home/jaime/compartida/codigo/minciencias/{item['medio']}/{item['titulo']}.txt","w+")
        archivo.write(f"titulo: {item['titulo']}\n\n")
        archivo.write(f"medio: {item['medio']}\n\n")
        archivo.write(f"numero: {item['numero']}\n\n")
        archivo.write(f"link: {item['link']}\n\n")
        archivo.write(f"fecha: {item['fecha']}\n\n")
        archivo.write(f"contenido principal: {item['contenido']}\n\n")
        archivo.write(f"contenido auxiliar: {item['contenido_auxiliar']}\n\n")
        archivo.close()
        return item
