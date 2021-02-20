import scrapy
from ..items import TextualItem
import site
site.addsitedir("/home/jaime/compartida/codigo/trabajo-minciencias")
from utils import procesar_peticion
from utils.reducir_dimension import reducir_dimension
class eafit(scrapy.Spider):
    name = 'eafit'
    start_urls = ["http://bitacora.eafit.edu.co/itinerarios/"]
    secciones = ["brujula","expidiciones","equipaje","experiencias","itinerarios"]
    def parse(self,response):
        links = []
        links.append(response.xpath("//div/p/a/@href").getall())
        #itinerario
        #links.append(procesar_peticion.eafit(1,10509,"ad23021",2791))
        #links.append(procesar_peticion.eafit(1,10509,"ad23021",2793))
        #links.append(procesar_peticion.eafit(1,10509,"ad23021",2825))
        #experiencias
        #links.append(procesar_peticion.eafit(1,12126,"4868ad26",2792))
        #links.append(procesar_peticion.eafit(1,12126,"4868ad26",2826))
        #links.append(procesar_peticion.eafit(1,12126,"4868ad26",2824))
        #links.append(procesar_peticion.eafit(1,12126,"4868ad26",2797))
        #brujula
        links.append(procesar_peticion.eafit(1,12224,"236ccb61",2795))
        links.append(procesar_peticion.eafit(1,12224,"236ccb61",2796))
        links.append(procesar_peticion.eafit(1,12224,"236ccb61",2821))
        links = reducir_dimension(links)
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        for seccion in self.secciones:
            if seccion == "itinerarios":
                paginacion = 0
                while paginacion <= 15:
                    aux = procesar_peticion.eafit(paginacion,10509,"637a27c",-1)
                    links.append(aux)
                    paginacion += 1
            else:
                next_page = f"http://bitacora.eafit.edu.co/{seccion}/"
                yield response.follow(url=next_page,callback=self.parse)

    def get_info(self,response,**kwargs):
        item = TextualItem()
        date = response.xpath("//ul/li[@itemprop]/a/span/text()").get()
        try:
            title = response.xpath("//h6/text()").getall()[0]
            title = title.strip()
        except:
            title = ""
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
        item["departamento"] = "Antioquia"
        yield item