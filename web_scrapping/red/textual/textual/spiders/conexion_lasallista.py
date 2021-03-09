import scrapy
from ..items import TextualItem
import sys

class conexion_lasallista(scrapy.Spider):
    name = 'conexion_lasallista'
    start_urls = ["http://conexion.lasallista.edu.co/?s=conflicto+armado"]
    secciones = ["conflicto+armado","memoria+de+las+victimas","proceso+de+paz"]

    def parse(self,response):
        links = response.xpath("//h3/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        
        for seccion in self.secciones:
            next_page = f"http://conexion.lasallista.edu.co/?s={seccion}"
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
        item["ciudad"] = "Bogota"
        item["nombre_medio"] = "conexion lasallista"
        item["universidad"] = "corporacion universitaria lasallista"
        item["departamento"] = "Cundinamarca"
        yield item
