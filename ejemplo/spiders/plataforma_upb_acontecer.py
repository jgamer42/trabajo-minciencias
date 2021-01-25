import scrapy
from ..items import EjemploItem
import sys

class plataforma_upb_acontecer(scrapy.Spider):
    name = 'plataforma_upb_acontecer'
    start_urls = ["https://plataforma.bucaramanga.upb.edu.co/acontecer"]
    page = 8
    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()
        for link in links:
            link = "https://plataforma.bucaramanga.upb.edu.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"https://plataforma.bucaramanga.upb.edu.co/acontecer?start={self.page}"
        if self.page <= 112:
            self.page = self.page + 8
            yield response.follow(url=next_page,callback=self.parse)
            
    def get_info(self,response,**kwargs):
        items = EjemploItem()
        items["link"]=kwargs["link"]
        items["numero"]=1
        items["medio"]=self.name
        title = response.xpath('//h1/text()').get()
        title = title.strip()
        date = response.xpath("//time/text()").get()
        date = date.strip()
        content = response.xpath("//div[@itemprop]/p/text()").getall()
        aux_content = response.xpath("//div[@itemprop]/p/strong/text() | //div[@itemprop]/p/em/text()").getall()
        aux_content = "".join(aux_content)
        content = "".join(content)
        items["titulo"] = title
        items["fecha"] = date
        items["contenido"] = content
        items["contenido_auxiliar"] = aux_content
        items["exploracion_general"] = True
        items["etiqueta_exploracion"] = None
        yield items