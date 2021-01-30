import scrapy
from ..items import EjemploItem
class eafit_carpita_roja(scrapy.Spider):
    name = 'eafit_carpita_roja'
    start_urls = ["http://bitacora.eafit.edu.co/carpita/"]
    def parse(self,response):
        links = response.xpath("//div[@class='raven-post-title']/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
              
    def get_info(self,response,**kwargs):
        item = EjemploItem()
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
        item["medio"] = self.name
        item["exploracion_general"] = True
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Medellin"
        item["nombre_medio"] = "bitacora"
        item["universidad"] = "eafit"
        yield item