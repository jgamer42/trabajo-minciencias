import scrapy
from ..items import EjemploItem
import sys

class tadeo(scrapy.Spider):
    name = 'tadeo'
    start_urls = ["https://www.utadeo.edu.co/es/search/node/%22conflicto%20armado%22"]
    page = 1
    def parse(self,response):
        a = response.xpath('//h3[@class="title"]/a/@href').getall()
        i = 0
        for link in a :
            i = i + 1
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link,"i":i})
            
        next_page = f"https://www.utadeo.edu.co/es/search/node/%22conflicto%20armado%22?page={self.page}"
        if self.page <= 44:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
            
    def get_info(self,response,**kwargs):
        items = EjemploItem()
        items["link"]=kwargs["link"]
        items["numero"]=kwargs["i"]
        items["medio"]=self.name
        title = response.xpath('//div[@class="field-item even"]/text()').getall()[1]
        date = response.xpath('//span[@class="date-display-single"]/text()').get()
        content = response.xpath('//p[@class]/text()').getall()
        if content == []:
            content = response.xpath('//div[@class="field-item even"]/p/text()').getall()
        aux_content = response.xpath('//strong/text()').getall()
        aux_content = "".join(aux_content)
        content = "".join(content)
        items["titulo"] = title
        items["fecha"] = date
        items["contenido"] = content
        items["contenido_auxiliar"] = aux_content
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        yield items




