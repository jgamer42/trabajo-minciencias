import scrapy
from ..items import TextualItem
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
        item = TextualItem()
        title = response.xpath("//div/h1/span/span/text()").getall()[1]
        title = title.replace("/","")
        title = title.strip()
        content = response.xpath("//article/div/div/div/div/p/span/text()").getall()
        content = " ".join(content)
        aux = response.xpath("//article/div/div/div/div/p/span/em/strong/text()").getall()
        aux = " ".join(aux)
        date = kwargs["link"].split("/")
        date = date[5:8]
        date = list(reversed(date))
        date = "/".join(date)
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["carpeta"] = self.name
        item["exploracion_general"] = True
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Medellin"
        item["nombre_medio"] = "contexto"
        item["universidad"] = "bolivariana de medellin"
        item["departamento"] = "Antioquia"
        
        yield item