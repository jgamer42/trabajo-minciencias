import scrapy
from ..items import EjemploItem
import site
site.addsitedir("/home/jaime/compartida/codigo/trabajo-minciencias/utils")
from utils import procesar_peticion
from utils.reducir_dimension import reducir_dimension

class uniminutoradio(scrapy.Spider):
    name = 'uniminutoradio'
    start_urls = ["https://www.uniminutoradio.com.co/?s=conflicto+armado"]

    def parse(self,response):
        links = []
        links.append(response.xpath("//h3/a/@href").getall())
        i = 2
        while i <= 37:
            links.append(procesar_peticion.uniminuto(i))
            i += 1
        links = reducir_dimension(links)
        
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//div/h1[@class='tdb-title-text']/text()").get()
        content = response.xpath("//div[@class='tdb-block-inner td-fix-index']/p/text()").getall()
        aux = response.xpath("//div[@class='tdb-block-inner td-fix-index']/h2/text()").getall()
        date = response.xpath('//div/time/text()').get()
        content = " ".join(content)
        aux = " ".join(aux)
        title = title.strip()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bogota"
        item["nombre_medio"] = "uniminutoradio"
        item["universidad"] = "uniminuto"
        yield item