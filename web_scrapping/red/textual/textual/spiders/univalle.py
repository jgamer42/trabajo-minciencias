import scrapy
from ..items import TextualItem
import sys

class univalle(scrapy.Spider):
    name = 'univalle'
    start_urls = ["http://ciudadvaga.univalle.edu.co/page/1/?s=conflicto+armado"]
    secciones = {"conflicto+armado":3,"memoria":5,"victimas":4,"proceso+de+paz":4,"paz":6}

    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()
        titulos = response.xpath("//header/h2/a/text()").getall()
        i = 0
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link,"titulo":titulos[i]})
            i += 1            
        for seccion in self.secciones.keys():
            i = 0
            while i <= self.secciones[seccion]:
                next_page = f"http://ciudadvaga.univalle.edu.co/page/{i}/?s={seccion}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)
   



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["titulo"] = kwargs["titulo"]
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["carpeta"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Cali"
        item["nombre_medio"] = "ciudad_vaga"
        item["universidad"] = "univalle"
        item["departamento"] = "Valle del cauca"

        yield item
