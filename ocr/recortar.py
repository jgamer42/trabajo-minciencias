from PyPDF2 import PdfFileReader,PdfFileWriter
import pandas as pd

def recortar(archivo,paginas):
    pdf_file = f"../corpus/red/pdfs_originales/{archivo}.pdf"
    pdf = PdfFileReader(pdf_file)
    pages = pdf.getNumPages()
    writer = PdfFileWriter()
    try:
        page = pdf.getPage(int(paginas)-1)
        output = f"{archivo}[{str(paginas)}].pdf"
        writer.addPage(page)
        with open(output,"wb") as out:
            writer.write(out)
    except:
        print("fallo",archivo,paginas,pages)
    

data = pd.read_csv("modelo.csv")
nombres = data["nombre"]
paginas = data["paginas"]
links = data["link"]
i = 0
for nombre in nombres:
    if nombre == "plataforma_35" or nombre == "contexto_37":
        try:
            recortar(nombre,paginas[i])
        except:
            print(f"fallo {nombre} {paginas[i]}")
    else:
        pass
        
    i = i + 1
