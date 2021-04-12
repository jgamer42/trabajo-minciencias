import scrapy
from ..items import TextualItem
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
        links.append(procesar_peticion.uniminuto(37,"tdi_84_966","conflicto armado"))
        links.append(procesar_peticion.uniminuto(55,"tdi_84_6a0","proceso de paz"))
        links.append(procesar_peticion.uniminuto(12,"tdi_84_d40","memoria de las victimas"))
        i = 0
        links = reducir_dimension(links)
        for link in links:
            if link == None:
                continue
            else:
                yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})



    def get_info(self,response,**kwargs):
        print("entro\n\n")
        item = TextualItem()
        try:
            title = response.xpath("//div/h1[@class='tdb-title-text']/text()").get()
            title = title.strip()
        except:
            title = ""
        content = response.xpath("//div[@class='tdb-block-inner td-fix-index']/p/text() | //div[@dir]/text() | //div[@class='tdb-block-inner td-fix-index']/div/div/p/strong/text()|//div[@class='tdb-block-inner td-fix-index']/div/p/text()|//div[@class='tdb-block-inner td-fix-index']/p/text() |//div[@class='tdb-block-inner td-fix-index']/p/strong/text()").getall()
        aux = response.xpath("//div[@class='tdb-block-inner td-fix-index']/h2/text() | //p/span/text() | //p/em/text()").getall()
        date = response.xpath('//div/time/text()').get()
        content = " ".join(content)
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["carpeta"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Bogota"
        item["nombre_medio"] = "uniminutoradio"
        item["universidad"] = "uniminuto"
        item["departamento"] = "Cundinamarca"
        yield item