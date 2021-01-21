import scrapy
from ..items import EjemploItem
class bolivarianaMedellin(scrapy.Spider):
    name = 'bolivarianaMedellin'
    start_urls = ["https://periodicocontexto.wixsite.com/contexto/inicio/page/1"]
    page = 2
    def parse(self,response):
        links = response.xpath("//article/div/a/@href").getall()[1:-3]
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        next_page = f"https://periodicocontexto.wixsite.com/contexto/inicio/page/{self.page}"
        if self.page <= 31:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
        
        

    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//div/h1/span/span/text()").getall()[1]
        title = title.strip()
        content = response.xpath("//article/div/div/div/div/p/span/text()").getall()
        content = " ".join(content)
        aux = response.xpath("//article/div/div/div/div/p/span/em/strong/text()").getall()
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"] = self.name
        item["exploracion_general"] = True
        item["etiqueta_exploracion"] = None
        yield item