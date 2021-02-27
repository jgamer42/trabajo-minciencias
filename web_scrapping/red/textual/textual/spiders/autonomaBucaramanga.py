import scrapy
from ..items import TextualItem
import sys
#links= 
#title = //div[@class="field-item even"]/text()
#date = //span[@class="date-display-single"]/text()
#texto = //p[@class]text()
#texto_auxiliar = //strong/text()

class autonomaBucaramanga(scrapy.Spider):
    name = 'autonomaBucaramanga'
    start_urls = ["https://www.periodico15.com/page/1/?s=conflicto+armado"]
    secciones = {"conflicto+armado":19,"memoria":17,"victimas":18,"proceso+de+paz":19,"paz":34}

    def parse(self,response):
        links = response.xpath("//h3/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        
        for seccion in self.secciones.keys():
            i = 1
            while i <= self.secciones[seccion]:
                next_page = f"https://www.periodico15.com/page/{i}/?s={seccion}"
                i += 1
                yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text() | //div[@class='td-post-content td-pb-padding-side']/div/text()").getall()
        aux = response.xpath("//div/p/strong/text() | //div/p/span/text() | //div/p/b/text()").getall()
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
        item["nombre_medio"] = "periodico_15"
        item["universidad"] = "autonoma de bucaramanga"
        item["departamento"] = "Santander"
        yield item
