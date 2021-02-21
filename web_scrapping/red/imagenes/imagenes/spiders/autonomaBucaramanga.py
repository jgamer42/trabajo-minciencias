import scrapy
from ..items import ImagenesItem
import sys


class autonomaBucaramanga(scrapy.Spider):
    name = 'autonomaBucaramanga'
    start_urls = ["https://www.periodico15.com/page/1/?s=conflicto+armado"]
    page = 1

    def parse(self,response):
        links = response.xpath("//h3/a/@href").getall()
        for link in links:
            yield response.follow(url=link,callback=self.get_info)

        next_page = f"https://www.periodico15.com/page/{self.page}/?s=conflicto+armado"
        if self.page <= 19:
            self.page = self.page + 1
            yield response.follow(url=next_page,callback=self.parse)
   



    def get_info(self,response,**kwargs):
        item = ImagenesItem()
        item["imagen"] = response.xpath("//div[@class='td-post-featured-image']/a/img/@src | //figure/img/@src").getall()
        item["universidad"] = self.name
        yield item
