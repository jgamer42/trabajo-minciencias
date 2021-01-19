import scrapy
from ..items import EjemploItem
import sys
class uniminutoMedellin(scrapy.Spider):
    name = 'uniminutoMedellin'
    start_urls = ["http://norteurbanodigital.com/?s=conflicto+armado"]
    page = 1

    def parse(self,response):
        links = response.xpath("//article/header/h2/a/@href").getall()
        for link in links:
            print(f"\n\n\n\n\n{link}\n\n\n\n")
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
   



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        content = content.strip()
        aux = " ".join(aux)
        date = response.xpath("//time/text()").getall()[0]
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = True
        item["etiqueta_exploracion"] = None
        yield item
