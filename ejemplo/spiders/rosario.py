import scrapy
from ..items import EjemploItem
import sys

class tadeo(scrapy.Spider):
    name = 'rosario'
    start_urls = ["https://plazacapital.co/search/conflicto-armado/page-1?t=1609619674793&tpl=search"]
    page = 1

    def parse(self,response):
        links = response.xpath("//div/h2/a/@href").getall()
        for link in links:
            link = "https://plazacapital.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})
            
        next_page = f"https://plazacapital.co/search/conflicto-armado/page-{self.page}?t=1609619674793&tpl=search"
        if self.page <= 11:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//div/h2/text()").get()
        date = response.xpath("//div/div[@class='item-info-head']/span/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        aux = "".join(aux)
        print(f"\n\n\n\n\n\n\n {content}")
        title = title.strip()
        date = date.strip()
        item["link"]=kwargs["link"]
        item["numero"]=1
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        yield item