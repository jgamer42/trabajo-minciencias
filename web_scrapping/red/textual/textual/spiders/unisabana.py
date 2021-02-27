import scrapy
from ..items import TextualItem
import sys

class unisabana(scrapy.Spider):
    name = 'unisabana'
    start_urls = ["https://www.unisabanamedios.com/search-results/q-conflicto-armado/qc-pages/page-1"]
    page = 1
    def parse(self,response):
        links = response.xpath('//div[@data-hook]/ul/li/a/@href').getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
        next_page = f"https://www.unisabanamedios.com/search-results/q-conflicto-armado/qc-pages/page-{self.page}"
        if self.page <= 19:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
    
    def get_info(self,response,**kwargs):
        item = TextualItem()
        try:
            title = response.xpath("//div/div/h4/span/span/span/text()").getall()[0]
        except:
            title = response.xpath("//div/div/h1/span/text()").get()
        content = response.xpath("//div/p/text()").getall()
        content = " ".join(content)
        content = content.strip()
        aux = response.xpath("//div/p/strong/text()").getall()
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bogota"
        item["nombre_medio"] = "unisabana_medios"
        item["universidad"] = "unisabana"
        item["departamento"] = "Cundinamarca" 
        yield item



