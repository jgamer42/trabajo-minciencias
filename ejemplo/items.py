# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EjemploItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    medio = scrapy.Field()
    fecha = scrapy.Field()
    numero = scrapy.Field()
    contenido = scrapy.Field()
    contenido_auxiliar = scrapy.Field()
    link = scrapy.Field()
    titulo = scrapy.Field()