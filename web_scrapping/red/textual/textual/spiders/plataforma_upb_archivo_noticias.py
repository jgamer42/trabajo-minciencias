import scrapy
from ..items import TextualItem
import sys

class plataforma_upb_archivo_noticias(scrapy.Spider):
    name = 'plataforma_upb_archivo_noticias'
    start_urls = ["https://plataforma.bucaramanga.upb.edu.co/archivo-articulos"]
    page = 10
    def parse(self,response):
        links = response.xpath("//h3[@class='catItemTitle']/a/@href").getall()
        for link in links:
            link = "https://plataforma.bucaramanga.upb.edu.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"https://plataforma.bucaramanga.upb.edu.co/archivo-articulos?start={self.page}"
        if self.page <= 120:
            self.page = self.page + 10
            yield response.follow(url=next_page,callback=self.parse)
            
    def get_info(self,response,**kwargs):
        items = TextualItem()
        items["link"]=kwargs["link"]
        items["medio"]=self.name
        title = response.xpath('//h2/text()').get()
        title = title.strip()
        date = response.xpath("//span[@class='itemDateCreated']/text()").get()
        date = date.strip()
        content = response.xpath("//div[@class='itemFullText']/p/text()").getall()
        aux_content = response.xpath("//div[@class='itemFullText']/p/strong/text() | //div[@class='itemFullText']/p/em/text()").getall()
        aux_content = "".join(aux_content)
        content = "".join(content)
        items["titulo"] = title
        items["fecha"] = date
        items["contenido"] = content
        items["contenido_auxiliar"] = aux_content
        items["exploracion_general"] = True
        items["etiqueta_exploracion"] = None
        items["ciudad"] = "Bucaramanga"
        items["nombre_medio"] = "plataforma"
        items["universidad"] = "bolivariana bucaramanga"
        item["departamento"] = "Santander"
        
        yield items
