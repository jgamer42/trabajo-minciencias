import scrapy
from ..items import TextualItem
import sys

class fundacionUniversitariaPopayan(scrapy.Spider):
    name = 'fundacionUniversitariaPopayan'
    start_urls = ["http://elclaustro.com.co/elclaustro/page/1/?s=conflicto+armado"]
    secciones = {"conflito+armado":2,"memoria+de+las+victimas":1,"proceso+de+paz":4,}

    def parse(self,response):
        links = response.xpath("//article/div/header/h2/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        for seccion in self.secciones.keys():
            i = 1
            while i <= self.secciones[seccion]:
                next_page = f"http://elclaustro.com.co/elclaustro/page/{i}/?s={seccion}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//header/h1/text()").get()
        try:
            date = response.xpath("//header/div/span/a/time/text()").getall()[0]
        except:
            date = "00/00/0000"
        content = response.xpath("//article/div/p/text()").getall()
        aux = response.xpath("//article/div/p/strong/text()").getall()
        content = " ".join(content)
        aux = "".join(aux)
        title = title.strip()
        date = date.strip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["carpeta"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Popayan"
        item["nombre_medio"] = "el_claustro"
        item["universidad"] = "fundacion universitaria de popayan"
        item["departamento"] = "Cauca"
        yield item