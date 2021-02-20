import scrapy
from ..items import TextualItem
import sys

class santiagoCali(scrapy.Spider):
    name = 'santiagoCali'
    start_urls = ["http://utopicos.com.co/index.php/component/search/?searchword=conflicto%20armado&searchphrase=all&limitstart=0"]
    page = 20

    def parse(self,response):
        links = response.xpath("//dt/a/@href").getall()
        for link in links:
            link = "http://utopicos.com.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"http://utopicos.com.co/index.php/component/search/?searchword=conflicto%20armado&searchphrase=all&limitstart={self.page}"
        if self.page <= 40:
            self.page = self.page + 20
            yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//h1/a/text()").get()
        title = title.strip()
        date = response.xpath("//time/text()").getall()
        if (date != None) and (len(date)>=1):
            date = date[0]
        else:
            date = "no disponible"
        content = response.xpath("//section/p/text() | //section/div/text() | //section/div/font/text() | //p/font/font/font/font/text()").getall()
        aux = response.xpath("//section/p/strong/text() | //section/p/strong/em/text() | //p/span/span/text() | //p/span/text()").getall()
        content = " ".join(content)
        aux = "".join(aux)
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
        item["ciudad"] = "Cali"
        item["nombre_medio"] = "utopicos"
        item["universidad"] = "universidad santiago de cali"
        item["departamento"] = "Valle del Cauca"

        yield item