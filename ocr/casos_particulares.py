import os 
import re 
from PyPDF2 import PdfFileReader,PdfFileWriter
def identificar(ruta_base):
    salida = []
    os.chdir(ruta_base+"/corpus/red/pdfs_recortes")
    elementos = os.listdir()
    for elemento in elementos:
        aux = elemento.split("[")
        aux2 = aux[1].split(".")
        paginas = aux2[0].replace("[","")
        paginas = aux2[0].replace("]","")
        if "-" in paginas:
            paginas = paginas.split("-")
            paginas = list(map(int,paginas))
            diferencia = paginas[1]-paginas[0]
            if diferencia > 2:
                salida.append(elemento)
        else:
            pass
    return salida

def recortar(nombre,pos,pdf):
    page = pdf.getPage(pos)
    writer = PdfFileWriter()
    salida = nombre+f"[{pos}]_caso.pdf"
    writer.addPage(page)
    with open(salida,"wb")as out:
        writer.write(out)



def procesar():
    base =  os.path.dirname(os.getcwd())
    casos = identificar(base)
    os.chdir(base)
    for caso in casos:
            
        pdf_file = base+f"/corpus/red/pdfs_recortes/{caso}"
        pdf = PdfFileReader(pdf_file)
        pages = pdf.getNumPages()
        i = 0
        while i < pages:
            nombre = caso.split(".")[0]
            nombre = nombre.split("/")[-1]
            nombre = nombre.split("[")[0]
            recortar(nombre,i,pdf)
            i += 1
        
    
#print(identificar(os.path.dirname(os.getcwd())))