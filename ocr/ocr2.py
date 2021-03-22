import requests


def ocr_space_file(filename, api_key='8592c0d84388957'):
    payload = {'isOverlayRequired': False,
               'apikey': api_key,
               'language':'spa',
               'detectOrientation':True,
               'scale':True,
               'OCREngine':1
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    a=r.json()
    print(a['ParsedResults'][0]["ParsedText"])
    #return r.content.decode()

#ocr_space_file("fotos/uniminuto_edicion34V2_01:05:15*.jpg")
#ocr_space_file("fotos/uniminuto_edicion38V3_01:05:16*.jpg")
# revisar estos dos archivos
ocr_space_file("fotos/prueba2.jpg")

#ern =  m
#