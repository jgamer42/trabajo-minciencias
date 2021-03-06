import scrapy
from ..items import TextualItem
class eafit_carpita_roja(scrapy.Spider):
    name = 'eafit_carpita_roja'
    start_urls = ["http://bitacora.eafit.edu.co/carpita/"]
    def parse(self,response):
        links = response.xpath("//div[@class='raven-post-title']/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
              
    def get_info(self,response,**kwargs):
        item = TextualItem()
        date = response.xpath("//ul/li[@itemprop]/a/span/text()").get()
        date = date.strip()
        title = response.xpath("//h6/text()").getall()[0]
        title = title.strip()
        content = response.xpath("//p/text()").getall()
        content = " ".join(content)
        aux = response.xpath("//p/strong/text() | //div[@class='elementor-testimonial-content']/text()").getall()
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["carpeta"] = self.name
        item["exploracion_general"] = None
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Medellin"
        item["nombre_medio"] = "bitacora"
        item["universidad"] = "eafit"
        item["departamento"] = "Antioquia"
        yield item