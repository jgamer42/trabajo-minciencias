import scrapy
from ..items import TextualItem
import sys

class plataforma_upb_archivo_opinion(scrapy.Spider):
    name = 'plataforma_upb_archivo_opinion'
    start_urls = ["https://plataforma.bucaramanga.upb.edu.co/archivo-opinion"]
    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()
        for link in links:
            link = "https://plataforma.bucaramanga.upb.edu.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
    def get_info(self,response,**kwargs):
        items = TextualItem()
        items["link"]=kwargs["link"]
        items["medio"]=self.name
        title = response.xpath('//h1/text()').get()
        title = title.strip()
        date = response.xpath("//time/text()").get()
        date = date.strip()
        content = response.xpath("//div[@itemprop]/p/text()").getall()
        aux_content = response.xpath("//div[@itemprop]/p/strong/text() | //div[@itemprop]/p/em/text()").getall()
        aux_content = "".join(aux_content)
        content = "".join(content)
        items["titulo"] = title
        items["fecha"] = date
        items["contenido"] = content
        items["contenido_auxiliar"] = aux_content
        items["exploracion_general"] = True
        items["etiqueta_exploracion"] = None
        items["ciudad"] = "Bucaramanga"
        items["nombre_medio"] = "plataforma"
        items["universidad"] = "bolivariana bucaramanga"
        item["departamento"] = "Santander"
        yield items