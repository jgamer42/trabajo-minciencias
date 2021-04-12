from PyPDF2 import PdfFileReader,PdfFileWriter
import pandas as pd

def recortar(archivo,paginas):
    pdf_file = f"../corpus/red/pdfs_originales/{archivo}.pdf"
    pdf = PdfFileReader(pdf_file)
    pages = pdf.getNumPages()
    writer = PdfFileWriter()
    try:
        page = pdf.getPage(int(paginas)-1)
        output = f"{archivo}-{str(paginas)}.pdf"
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
    if "-" in paginas[i]:
        pass
    else:
        try:
            recortar(nombre,paginas[i])
        except:
            print(f"fallo {nombre} {paginas[i]}")
        #if "contexto" in nombre:
        #    print(f"{nombre},{paginas[i]},{links[i]}")
        #    try:
        #        print("funciona")
        #        recortar(nombre,paginas[i])
        #    except:
        #        print("fallo")

    i = i + 1
