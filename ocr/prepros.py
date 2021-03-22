from PIL import Image 

def recortar(imagen):
    nombre = imagen.split(".")[0]
    im = Image.open(imagen)
    width, heigth = im.size
    hoja1 = im.crop((0,0,int(width/2),heigth))
    hoja2 = im.crop((int(width/2),0,width,heigth))
    hoja1.save(f"{nombre}_hoja1.jpg",quality=100,subsampling=0)
    hoja2.save(f"{nombre}_hoja2.jpg",quality=100,subsampling=0)
