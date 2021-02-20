import scrapy
from ..items import TextualItem
import sys

class tadeo(scrapy.Spider):
    name = 'tadeo'
    start_urls = ["https://www.utadeo.edu.co/es/search/node/%22conflicto%20armado%22"]
    page = 1
    def parse(self,response):
        a = response.xpath('//h3[@class="title"]/a/@href').getall()
        for link in a :
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"https://www.utadeo.edu.co/es/search/node/%22conflicto%20armado%22?page={self.page}"
        if self.page <= 44:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
            
    def get_info(self,response,**kwargs):
        items = TextualItem()
        items["link"]=kwargs["link"]
        items["medio"]=self.name
        title = response.xpath('//div[@class="field-item even"]/text()').getall()[1]
        date = response.xpath('//span[@class="date-display-single"]/text()').get()
        content = response.xpath('//p[@class]/text() | //div[@class="field-item even"]/p/text() | //div[@style="text-align: justify;"]/p/text() | //div[@class="field-item even" and @property]/div[@class]/text()').getall()
        aux_content = response.xpath('//div/p/span/text() | //p/span/text() | //strong/text() | //td/p/text()').getall()
        aux_content = "".join(aux_content)
        content = "".join(content)
        items["titulo"] = title
        items["fecha"] = date
        items["contenido"] = content
        items["contenido_auxiliar"] = aux_content
        items["exploracion_general"] = False
        items["etiqueta_exploracion"] = None
        items["ciudad"] = "Bogota"
        items["nombre_medio"] = "crossmedialab"
        items["universidad"] = "tadeo"
        items["departamento"] = "Cundinamarca"

        yield items




