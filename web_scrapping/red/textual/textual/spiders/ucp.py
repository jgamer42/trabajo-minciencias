import scrapy
from ..items import TextualItem
import sys

class ucp(scrapy.Spider):
    name = 'ucp'
    start_urls = ["https://www.otunmedialab.com/elcronista-2019"]
    secciones = ["2019","2017","2018"]


    def parse(self,response):
        links = response.xpath("//div/a/@href").getall()[1:]
        print("\n\n\n\n",links,"\n\n\n\n")
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
        for seccion in self.secciones:
            next_page = f"https://www.otunmedialab.com/elcronista-{seccion}"
            yield response.follow(url=next_page,callback=self.parse)


    def get_info(self,response,**kwargs):
        item = TextualItem()
        title = response.xpath("//div/span/text()").get()
        content = response.xpath("//p/span/text()").getall()
        content = " ".join(content)
        title = title.lstrip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = "no disponible"
        item["contenido"] = content
        item["contenido_auxiliar"] = "no disponible en este medio"
        item["carpeta"]=self.name
        item["exploracion_general"] = True
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Pereira"
        item["nombre_medio"] = "otun media lab"
        item["universidad"] = "universidad catolica de Pereira"
        item["departamento"] = "Risaralda"
        yield item
