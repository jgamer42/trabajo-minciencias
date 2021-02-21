import scrapy
from ..items import ImagenesItem
import sys

class bolivarianaBucaramanga(scrapy.Spider):
    name = 'bolivarianaBucaramanga'
    start_urls = ["https://estacionv.bucaramanga.upb.edu.co/buscar?searchword=conflicto%20armado&ordering=newest&searchphrase=all&areas[0]=categories&areas[1]=contacts&areas[2]=content&areas[3]=newsfeeds&areas[4]=weblinks&areas[5]=k2"]

    def parse(self,response):
        links = response.xpath("//article/h1/a/@href").getall()
        for link in links:
            link = "https://estacionv.bucaramanga.upb.edu.co"+link
            yield response.follow(url=link,callback=self.get_info)
   



    def get_info(self,response,**kwargs):
        item = ImagenesItem()
        item["imagen"] = response.xpath("//img/@src").getall()
        print("\n\n",item['imagen'],"\n\n")
        item["universidad"] = self.name
        yield item