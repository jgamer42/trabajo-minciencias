# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class ImagenesPipeline:
    def process_item(self, item, spider):
        for elemento in item["imagen"]:
            print(f" \n\n /home/jaime/compartida/codigo/trabajo-minciencias/corpus/red/imagenes/{item['universidad']}\n\n")
            os.chdir(f"/home/jaime/compartida/codigo/trabajo-minciencias/corpus/red/imagenes/{item['universidad']}")
            os.system(f"wget {elemento}")
        return item
