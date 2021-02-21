import scrapy
from ..items import TextualItem

class plataforma_upb(scrapy.Spider):
    name = 'plataforma_upb'
    start_urls = ["https://plataforma.bucaramanga.upb.edu.co/comunidad-viva"]
    secciones = {"acontecer":122,"comunidad-viva":24,"cultural":24,"en-el-juego":8,"prospectiva":0,"frente-a-frente":0,"zona-de-paz":8}
    page = 8
    def parse(self,response):
        links = response.xpath("//h2/a/@href").getall()   
        for link in links:
            link = "https://plataforma.bucaramanga.upb.edu.co"+link
            yield response.follow(url=link,callback=self.get_info,cb_kwargs={"link":link})

        for seccion in self.secciones.keys():
            self.page = 0
            limite = self.secciones[seccion]
            while self.page <= limite:
                next_page = f"https://plataforma.bucaramanga.upb.edu.co/{seccion}?start={self.page}"
                self.page = self.page + 8
                yield response.follow(url=next_page,callback=self.parse)

    def get_info(self,response,**kwargs):
        items = TextualItem()
        items["link"]=kwargs["link"]
        items["medio"]=self.name
        title = response.xpath('//h1/text()').get()
        title = title.strip()
        date = response.xpath("//time/text()").get()
        date = date.strip()
        content = response.xpath("//div[@itemprop]/p/text()").getall()
        aux_content = response.xpath("//div[@itemprop]/p/strong/text() | //div[@itemprop]/p/em/text()").getall()
        aux_content = "".join(aux_content)
        content = "".join(content)
        items["titulo"] = title
        items["fecha"] = date
        items["contenido"] = content
        items["contenido_auxiliar"] = aux_content
        items["exploracion_general"] = True
        items["etiqueta_exploracion"] = None
        items["ciudad"] = "Bucaramanga"
        items["nombre_medio"] = "plataforma"
        items["universidad"] = "bolivariana bucaramanga"
        items["departamento"] = "Santander"
        yield items