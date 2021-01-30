import scrapy
from ..items import EjemploItem
import sys
#links= 
#title = //div[@class="field-item even"]/text()
#date = //span[@class="date-display-single"]/text()
#texto = //p[@class]text()
#texto_auxiliar = //strong/text()

class autonomaBucaramanga(scrapy.Spider):
    name = 'autonomaBucaramanga'
    start_urls = ["https://www.periodico15.com/page/1/?s=conflicto+armado"]
    page = 1

    def parse(self,response):
        links = response.xpath("//h3/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        next_page = f"https://www.periodico15.com/page/{self.page}/?s=conflicto+armado"
        if self.page <= 19:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
   



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        date = response.xpath("//time/text()").get()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bucaramanga"
        item["nombre_medio"] = "periodico 15"
        item["universidad"] = "autonoma de bucaramanga"
        yield item
