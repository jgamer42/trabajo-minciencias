import scrapy
from ..items import EjemploItem
class plataforma_upb_zona_paz(scrapy.Spider):
    name = 'plataforma_upb_zona_paz'
    start_urls = ["https://plataforma.bucaramanga.upb.edu.co/zona-de-paz"]
    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()
        for link in links:
            link = "https://plataforma.bucaramanga.upb.edu.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
              
    def get_info(self,response,**kwargs):
        item = EjemploItem()
        date = response.xpath("//time/text()").get()
        date = date.strip()
        title = response.xpath("//h1/text()").get()
        title = title.strip()
        content = response.xpath("//div[@itemprop]/p/text()").getall()
        content = " ".join(content)
        aux = response.xpath("//div[@itemprop]/p/strong/text()").getall()
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