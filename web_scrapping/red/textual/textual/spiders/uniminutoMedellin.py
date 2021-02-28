import scrapy
from ..items import TextualItem
import sys
class uniminutoMedellin(scrapy.Spider):
    name = 'uniminutoMedellin'
    start_urls = ["http://norteurbanodigital.com/?s=conflicto+armado"]
    secciones = {"conflicto+armado":1,"memoria":1,"victimas":1,"proceso+de+paz":1,"paz":2}

    def parse(self,response):
        links = response.xpath("//article/header/h2/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
        for seccion in self.secciones.keys():
            i = 1
            while i <= self.secciones[seccion]:
                next_page = f"http://norteurbanodigital.com/page/{i}/?s={seccion}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        content = content.strip()
        aux = " ".join(aux)
        date = response.xpath("//time/text()").getall()[0]
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Medellin"
        item["nombre_medio"] = "norte_urbano"
        item["universidad"] = "uniminuto"
        item["departamento"] = "Antioquia"

        yield item
