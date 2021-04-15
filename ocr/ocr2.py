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
        print(r.json())
    a=r.json()
    #return a['ParsedResults'][0]["ParsedText"]


ocr_space_file("/home/jaime/compartida/codigo/trabajo-minciencias/corpus/red/pdfs_recortes_completos/universidadBoyaca/pretexto_2[48-51]-comprimido.pdf")