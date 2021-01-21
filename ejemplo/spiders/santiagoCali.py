import scrapy
from ..items import EjemploItem
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
        item = EjemploItem()
        title = response.xpath("//h1/a/text()").get()
        title = title.strip()
        date = response.xpath("//time/text()").getall()[0]
        content = response.xpath("//section/p/text()").getall()
        aux = response.xpath("//section/p/strong/text() | //section/p/strong/em/text()").getall()
        content = " ".join(content)
        aux = "".join(aux)
        title = title.strip()
        date = date.strip()
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        yield item