import scrapy
from ..items import TextualItem
import sys

class udea(scrapy.Spider):
    name = 'udea'
    start_urls = ["https://delaurbe.udea.edu.co/index.php/component/k2/itemlist/search?searchword=conflicto+armado&Itemid=138"]
    secciones = ["conflicto+armado","memoria","victimas","proceso+de+paz","paz"]

    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()
        for link in links:
            link = "https://delaurbe.udea.edu.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        for seccion in self.secciones:
            next_page = f"https://delaurbe.udea.edu.co/index.php/component/k2/itemlist/search?searchword={seccion}&Itemid=138"
            yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//h2[@class='itemTitle']/text()").get()
        date = response.xpath("////div/span/span/text()").getall()
        date = [i.strip() for i in date]
        date = " ".join(date)
        content = response.xpath("//div[@class='itemFullText']/p/text()").getall()
        content = " ".join(content)
        content = content.strip()
        aux = response.xpath("//div[@class='itemFullText']/p/span/text() | //div[@class='itemFullText']/blockquote/p/text() | //div[@class='itemFullText']/h2/text()").getall()
        aux = " ".join(aux)
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
        item["ciudad"] = "Medellin"
        item["nombre_medio"] = "de_la_urbe"
        item["universidad"] = "universidad de antioquia"
        item["departamento"] = "Antioquia"

        yield item