import scrapy
from ..items import EjemploItem
import sys
#links= 
#title = //div[@class="field-item even"]/text()
#date = //span[@class="date-display-single"]/text()
#texto = //p[@class]text()
#texto_auxiliar = //strong/text()

class tadeo(scrapy.Spider):
    name = 'univalle'
    start_urls = ["http://ciudadvaga.univalle.edu.co/page/1/?s=conflicto+armado"]
    page = 1

    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()
        titulos = response.xpath("//header/h2/a/text()").getall()
        i = 0
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link,"titulo":titulos[i]})
            i += 1

        next_page = f"http://ciudadvaga.univalle.edu.co/page/{self.page}/?s=conflicto+armado"
        if self.page <= 3:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
   



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = kwargs["titulo"]
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        yield item
