import scrapy
from ..items import EjemploItem
import sys

class bolivarianaBucaramanga(scrapy.Spider):
    name = 'bolivarianaBucaramanga'
    start_urls = ["https://estacionv.bucaramanga.upb.edu.co/buscar?searchword=conflicto%20armado&ordering=newest&searchphrase=all&areas[0]=categories&areas[1]=contacts&areas[2]=content&areas[3]=newsfeeds&areas[4]=weblinks&areas[5]=k2"]
    page = 1

    def parse(self,response):
        links = response.xpath("//article/h1/a/@href").getall()
        dates = response.xpath("//article/p/text()").getall()
        contador = 0
        for link in links:
            link = "https://estacionv.bucaramanga.upb.edu.co"+link
            date = dates[contador]
            contador = contador + 1
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link,"date":date})
   



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//article/h1/text()").get()
        content = response.xpath("//article/div/p/text()").getall()
        content = " ".join(content)
        print(f"\n\n\n\n\n\n\n {content}")
        title = title.lstrip()
        date = kwargs["date"].lstrip()
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = "no disponible en este medio"
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        yield item
