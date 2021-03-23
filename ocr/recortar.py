from PyPDF2 import PdfFileReader,PdfFileWriter
import pandas as pd

def recortar(archivo,paginas):
    pdf_file = f"../corpus/red/pdfs/{archivo}.pdf"
    pdf = PdfFileReader(pdf_file)
    pages = pdf.getNumPages()
    writer = PdfFileWriter()
    flag = True
    if (len(paginas)>=2):
        for page in range(pages):
            if(page >= int(paginas[0]) and page <= int(paginas[1])-1):
                p = pdf.getPage(page)
                writer.addPage(p)
    else:
        try:
            page = pdf.getPage(paginas[0]-1)
            writer.addPage(page)
        except:
            print(paginas[0],paginas[0]-1,pages)
            flag = False
    if flag:
        output = f"{archivo}{str(paginas)}.pdf"
        with open(output,"wb") as out:
            writer.write(out)

data = pd.read_csv("primera extraccion.csv")
nombres = data["nombre"]
paginas = data["paginas"]
i = 0
for nombre in nombres:
    limites = paginas[i].split("-")
    limites = [int(l) for l in limites]
    print(nombre,limites)
    recortar(nombre,limites)
    i = i + 1