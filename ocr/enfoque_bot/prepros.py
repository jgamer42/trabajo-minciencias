from PIL import Image 

def recortar_margen(imagen):
    nombre = imagen.split(".")[0]
    im = Image.open(imagen)
    width , heigth = im.size
    im = im.crop((160,0,width,heigth))
    im.save(f"{nombre}_recortada.jpg")
def recortar_hojas(imagen):
    nombre = imagen.split(".")[0]
    im = Image.open(imagen)
    width, heigth = im.size
    hoja1 = im.crop((0,0,int(width/2)-40,heigth))
    hoja2 = im.crop((int(width/2)+30,0,width,heigth))
    hoja1.save(f"{nombre}_hoja1.jpg",quality=100,subsampling=0)
    hoja2.save(f"{nombre}_hoja2.jpg",quality=100,subsampling=0)

def recortar_columnas_3(imagen):
    im = Image.open(imagen)
    width, heigth = im.size
    ancho_columna = int(width/3)
    c1 = im.crop((0,0,ancho_columna,heigth))
    c2 = im.crop((ancho_columna,0,2*ancho_columna,heigth))
    c3 = im.crop((2*ancho_columna,0,3*ancho_columna,heigth))
    #c2.show()
    salida = Image.new('RGB',(int(width/3),heigth*3+10), (250,250,250))
    salida.paste(c1,(0,0))
    salida.paste(c2,(0,heigth))
    salida.paste(c3,(0,2*heigth))
    #salida.show()
    salida.save("recorte.jpg")

#recortar_columnas_3("salida_16-17_recortada_hoja1.jpg")
#recortar_hojas("salida_16-17_recortada.jpg")
recortar_columnas_3("salida_16-17_recortada_hoja2.jpg")
#recortar_margen("salida_16-17.jpg")
