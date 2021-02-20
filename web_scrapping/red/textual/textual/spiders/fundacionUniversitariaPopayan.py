import scrapy
from ..items import TextualItem
import sys

class fundacionUniversitariaPopayan(scrapy.Spider):
    name = 'fundacionUniversitariaPopayan'
    start_urls = ["http://elclaustro.com.co/elclaustro/page/1/?s=conflicto+armado"]
    page = 1

    def parse(self,response):
        links = response.xpath("//article/div/header/h2/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"http://elclaustro.com.co/elclaustro/page/{self.page}/?s=conflicto+armado"
        if self.page <= 2:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//header/h1/text()").get()
        date = response.xpath("//header/div/span/a/time/text()").getall()[0]
        content = response.xpath("//article/div/p/text()").getall()
        aux = response.xpath("//article/div/p/strong/text()").getall()
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
        item["ciudad"] = "Popayan"
        item["nombre_medio"] = "el claustro"
        item["universidad"] = "fundacion universitaria de popayan"
        item["departamento"] = "Cauca"
        yield item