import scrapy
from ..items import EjemploItem
import site
site.addsitedir("/home/jaime/compartida/codigo/trabajo-minciencias/utils")
from utils import procesar_peticion
from utils.reducir_dimension import reducir_dimension
class eafit_brujula(scrapy.Spider):
    name = 'eafit_brujula'
    start_urls = ["http://bitacora.eafit.edu.co/brujula/"]
    def parse(self,response):
        links = []
        links.append(response.xpath("//div/p/a/@href").getall())
        #analisis
        links.append(procesar_peticion.eafit(1,12224,"236ccb61",2795))
        #opinion
        links.append(procesar_peticion.eafit(1,12224,"236ccb61",2796))
        #reseñas
        links.append(procesar_peticion.eafit(1,12224,"236ccb61",2821))
        links = reducir_dimension(links)
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
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"] = self.name
        item["exploracion_general"] = True
        item["etiqueta_exploracion"] = None
        yield item