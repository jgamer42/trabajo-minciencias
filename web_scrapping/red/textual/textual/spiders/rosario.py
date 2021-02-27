import scrapy
from ..items import TextualItem
import sys

class rosario(scrapy.Spider):
    name = 'rosario'
    start_urls = ["https://plazacapital.co/search/conflicto-armado/page-1"]
    secciones = {"conflicto-armado":11,"memoria":18,"victimas":22,"proceso-de-paz":7,"paz":40}

    def parse(self,response):
        links = response.xpath("//div/h2/a/@href").getall()
        for link in links:
            link = "https://plazacapital.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            

        for seccion in self.secciones.keys():
            i = 1
            while i <= self.secciones[seccion]:
                next_page = f"https://plazacapital.co/search/{seccion}/page-{i}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//div/h2/text()").get()
        date = response.xpath("//div/div[@class='item-info-head']/span/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text() | //div/p/span/text()").getall()
        content = " ".join(content)
        aux = "".join(aux)
        title = title.strip()
        date = date.strip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bogota"
        item["nombre_medio"] = "plaza_capital"
        item["universidad"] = "rosario"
        item["departamento"] = "Cundinamarca"
        yield item