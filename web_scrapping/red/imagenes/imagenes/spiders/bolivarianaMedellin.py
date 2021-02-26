import scrapy
from ..items import ImagenesItem
import site
site.addsitedir("../../../")
from utils.buscar_palabras import buscar_palabras
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
        contenido = response.xpath("//article/div/div/div/div/p/span/text()").getall()
        contenido = " ".join(contenido)
        validar, _= buscar_palabras(contenido)
        if validar: 
            item = ImagenesItem() 
            item["imagen"] = response.xpath("//div[@role='img']/img/@src").getall()
            item["universidad"] = self.name
            print(f"\n\n\n\n\n{item['imagen']}\n\n\n\n\n")
            yield item
        else:
            pass
