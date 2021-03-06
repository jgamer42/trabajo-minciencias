# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TextualItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    carpeta = scrapy.Field()
    fecha = scrapy.Field()
    contenido = scrapy.Field()
    contenido_auxiliar = scrapy.Field()
    link = scrapy.Field()
    titulo = scrapy.Field()
    exploracion_general = scrapy.Field()
    etiqueta_exploracion = scrapy.Field()
    ciudad = scrapy.Field()
    nombre_medio = scrapy.Field()
    universidad = scrapy.Field()
    departamento = scrapy.Field()
