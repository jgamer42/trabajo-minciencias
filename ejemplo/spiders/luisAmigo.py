import scrapy
from ..items import EjemploItem
import sys

class luisAmigo(scrapy.Spider):
    name = 'luisAmigo'
    start_urls = ["http://www.funlam.edu.co/sextante/?s=conflicto+armado"]

    def parse(self,response):
        links = response.xpath("//article/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//article/h2/text()").get()
        content = response.xpath("//article/div/p").getall()
        aux = response.xpath("//article/div/p/strong/text() | //article/div/p/span/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        title = title.strip()
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        yield item