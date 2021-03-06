import scrapy
from ..items import TextualItem
import sys
#links= 
#title = //div[@class="field-item even"]/text()
#date = //span[@class="date-display-single"]/text()
#texto = //p[@class]text()
#texto_auxiliar = //strong/text()

class autonomaBucaramanga(scrapy.Spider):
    name = 'periodico15_conflicto'
    start_urls = ["https://www.periodico15.com/category/conflicto/d-d-h-h/"]
    secciones = {"d-d-h-h":7,"justicia":3,"paz":3,"paz-2":0}

    def parse(self,response):
        links = response.xpath("//h3/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        for seccion in self.secciones.keys():
            i = 1
            while i <= self.secciones[seccion]:
                next_page = f"https://www.periodico15.com/category/conflicto/{seccion}/page/{i}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)

    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text() | //div[@class='td-post-content td-pb-padding-side']/div/text()").getall()
        aux = response.xpath("//div/p/strong/text() | //div/p/span/text() | //div/p/b/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        date = response.xpath("//time/text()").get()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["carpeta"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bucaramanga"
        item["nombre_medio"] = "periodico_15"
        item["universidad"] = "autonoma de bucaramanga"
        item["departamento"] = "Santander"
        yield item
