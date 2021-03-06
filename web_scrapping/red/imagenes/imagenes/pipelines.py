# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class ImagenesPipeline:
    base = os.getcwd()
    def process_item(self, item, spider):
        for elemento in item["imagen"]:
            ruta = os.path.realpath(f"../../../corpus/red/imagenes/{item['universidad']}")
            print(f"\n\n {ruta} \n\n")
            os.chdir(ruta)
            os.system(f"wget {elemento}")
            os.chdir(self.base)
        return item
