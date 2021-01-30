import scrapy
from ..items import EjemploItem
import sys

class universidadIbague(scrapy.Spider):
    name = 'universidadIbague'
    start_urls = ["https://www.elanzuelomedios.com/index.php/historias?searchword=conflicto%20armado&searchphrase=all&start=0"]
    page = 20

    def parse(self,response):
        links = response.xpath("//article/header/h1/a/@href").getall()
        for link in links:
            link = "https://www.elanzuelomedios.com"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"https://www.elanzuelomedios.com/index.php/historias?searchword=conflicto%20armado&searchphrase=all&start={self.page}"
        if self.page <= 20:
            self.page = self.page + 20
            yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//header/h1/text()").get()
        date = response.xpath("//time/@datetime").get()
        content = response.xpath("//article/div/p/strong/text() | //article/div/p/span/text() ").getall()
        content = " ".join(content)
        title = title.strip()
        date = date.strip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = "no disponible en este medio"
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Ibague"
        item["nombre_medio"] = "el anzuelo medios"
        item["universidad"] = "universidad de Ibague"
        yield item