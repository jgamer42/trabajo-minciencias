import scrapy
from ..items import TextualItem
import sys

class luisAmigo(scrapy.Spider):
    name = 'luisAmigo'
    start_urls = ["http://www.funlam.edu.co/sextante/?s=conflicto+armado"]
    secciones = {"conflicto+armado":1,"memoria":3,"victimas":1,"proceso+de+paz":1,"paz":2}
    def parse(self,response):
        links = response.xpath("//article/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
        for seccion in self.secciones.keys():
            i = 1
            while i <= self.secciones[seccion]:
                next_page = f"http://www.funlam.edu.co/sextante/?s={seccion}&paged={i}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)


    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//article/h2/text()").get()
        content = response.xpath("//article/div/p/text()").getall()
        aux = response.xpath("//article/div/p/strong/text() | //article/div/p/span/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        title = title.strip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Medellin"
        item["nombre_medio"] = "sextante_digital"
        item["universidad"] = "luis amigo"
        item["departamento"] = "Antioquia"
        yield item