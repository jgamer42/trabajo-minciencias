import scrapy
from ..items import EjemploItem
import sys
#links = //div[@data-hook]/ul/li/a/@href
#titulo = //div/div/h4/span/span/span/text()
#contenido = //div/p/text()
#texto_auxiliar = //strong/text()

class unisabana(scrapy.Spider):
    name = 'unisabana'
    start_urls = ["https://www.unisabanamedios.com/search-results/q-conflicto-armado/qc-pages/page-1"]
    page = 1
    def parse(self,response):
        links = response.xpath('//div[@data-hook]/ul/li/a/@href').getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
        next_page = f"https://www.unisabanamedios.com/search-results/q-conflicto-armado/qc-pages/page-{self.page}"
        if self.page <= 19:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
    
    def get_info(self,response,**kwargs):
        item = EjemploItem()
        try:
            title = response.xpath("//div/div/h4/span/span/span/text()").getall()[0]
        except:
            title = response.xpath("//div/div/h1/span/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = "no disponible en este medio"
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        yield item



