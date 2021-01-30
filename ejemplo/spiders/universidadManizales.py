import scrapy
from ..items import EjemploItem
import sys
#//div[@class="vc_column tdi_70_1f5 wpb_column vc_column_container tdc-column td-pb-span8"]/div/div/div/div/div/div/h3/a/@href
#//div[@class="vc_column tdi_70_20f  wpb_column vc_column_container tdc-column td-pb-span8"]/div/div/div/div/div/div/h3/a/@href
class universidadManizales(scrapy.Spider):
    name = 'universidadManizales'
    start_urls = ["https://umcentral.umanizales.edu.co/index.php/page/1/?s=conflicto+armado"]
    page = 1

    def parse(self,response):
        links = response.xpath("//div[@id and @class='tdc-row']/div/div[not(contains(@class,'td-is-sticky'))]/div/div/div/div/div/div/h3/a/@href").getall()
        for link in links:
            print(f"\n\n\n\n\n{link}\n\n\n\n")
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        next_page = f"https://umcentral.umanizales.edu.co/index.php/page/{self.page}/?s=conflicto+armado"
        if self.page <= 2:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
   



    def get_info(self,response,**kwargs):
        item = EjemploItem()
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div/p/text()").getall()
        aux = response.xpath("//div/p/strong/text()").getall()
        content = " ".join(content)
        aux = " ".join(aux)
        date = response.xpath("//header/div/span/time/text()").get()
        item["link"]=kwargs["link"]
        item["titulo"] = title
        item["fecha"] = date
        item["contenido"] = content
        item["contenido_auxiliar"] = aux
        item["medio"]=self.name
        item["exploracion_general"] = False
        item["etiqueta_exploracion"] = None
        item["ciudad"] = "Manizales"
        item["nombre_medio"] = "um central"
        item["universidad"] = "universidad de Manizales"
        yield item
