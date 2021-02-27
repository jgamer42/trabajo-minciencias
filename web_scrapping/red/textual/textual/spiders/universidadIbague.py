import scrapy
from ..items import TextualItem
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
        item = TextualItem()
        title = response.xpath("//header/h1/text()").get()
        date = response.xpath("//time/@datetime").get()
        content = response.xpath("//article/div/p/strong/text() | //article/div/p/span/text() | //div[contains(@style,'color: #222222; font-family: arial, sans-serif;')]/text() | //p[@style]/text()  | //div[@class='content clearfix']/p/text() | //font/p/text() | //p/span/text()").getall()
        content = " ".join(content)
        content = content.strip()
        aux = response.xpath("//span/strong/span/text() ").getall()
        aux = " ".join(aux)
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
        item["ciudad"] = "Ibague"
        item["nombre_medio"] = "el_anzuelo_medios"
        item["universidad"] = "universidad de Ibague"
        item["departamento"] = "Ibague"

        yield item