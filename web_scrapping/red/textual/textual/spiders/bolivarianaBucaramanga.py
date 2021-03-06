import scrapy
from ..items import TextualItem
import sys

class bolivarianaBucaramanga(scrapy.Spider):
    name = 'bolivarianaBucaramanga'
    start_urls = ["https://estacionv.bucaramanga.upb.edu.co/buscar?searchword=conflicto%20armado&ordering=newest&searchphrase=all&areas[0]=categories&areas[1]=contacts&areas[2]=content&areas[3]=newsfeeds&areas[4]=weblinks&areas[5]=k2"]
    secciones = ["conflicto%20armado","memoria","victimas","proceso%20de%20paz","paz"]


    def parse(self,response):
        links = response.xpath("//article/h1/a/@href").getall()
        dates = response.xpath("//article/p/text()").getall()
        contador = 0
        for link in links:
            link = "https://estacionv.bucaramanga.upb.edu.co"+link
            date = dates[contador]
            contador = contador + 1
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link,"date":date})
        for seccion in self.secciones:
            next_page = f"https://estacionv.bucaramanga.upb.edu.co/buscar?searchword={seccion}&ordering=newest&searchphrase=all&areas[0]=categories&areas[1]=contacts&areas[2]=content&areas[3]=newsfeeds&areas[4]=weblinks&areas[5]=k2"
            yield response.follow(url=next_page,callback=self.parse)


    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//article/h1/text()").get()
        content = response.xpath("//article/div/p/text()").getall()
        content = " ".join(content)
        title = title.lstrip()
        date = kwargs["date"].lstrip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = "no disponible en este medio"
        item["carpeta"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bucaramanga"
        item["nombre_medio"] = "estacion_V"
        item["universidad"] = "bolivariana bucaramanga"
        item["departamento"] = "Santander"
        yield item
