import scrapy
from ..items import TextualItem
import sys

class tadeo(scrapy.Spider):
    name = 'tadeo'
    start_urls = ["https://www.utadeo.edu.co/es/search/node/%22conflicto%20armado%22"]
    secciones = {"%22conflicto%armado%22":44,"memoria":197,"victimas":98,"proceso%20de%20paz":74,"paz":243}
    def parse(self,response):
        a = response.xpath('//h3[@class="title"]/a/@href').getall()
        for link in a :
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        for seccion in self.secciones.keys():
            i = 0
            while i <= self.secciones[seccion]:
                next_page = f"https://www.utadeo.edu.co/es/search/node/{seccion}?page={i}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)
            
    def get_info(self,response,**kwargs):
        items = TextualItem()
        items["link"]=kwargs["link"]
        items["medio"]=self.name
        try:
            title = response.xpath('//div[@class="field-item even"]/text()').getall()[1]
        except:
            title = "error"
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




