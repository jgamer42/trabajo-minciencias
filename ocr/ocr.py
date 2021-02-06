import requests
import json
params ={
    'apikey' : "OCRP8421898A",
    'url' : "https://plataforma.bucaramanga.upb.edu.co/images/archivo/pdf/edicion-41.pdf",
    'language' : "spa",
    'scale' : "true",
    'isCreateSearchablePdf' : "true",
    'isSearchablePdfHideTextLayer' : "true"
}
url = "https://apipro1.ocr.space/parse/image"
datos = requests.post(url, data=params)
post = json.loads(datos.text)
for texto in post["ParsedResults"]:
    print(texto["ParsedText"])

print(texto["SearchablePDFURL"])