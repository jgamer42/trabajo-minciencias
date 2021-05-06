import requests


def ocr_space_file(filename, api_key=''):
    payload = {'isOverlayRequired': False,
               'apikey': api_key,
               'language':'spa',
               'detectOrientation':True,
               'scale':True,
               'OCREngine':1
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://apipro1.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    a=r.json()
    try:
        return a['ParsedResults'][0]["ParsedText"]
    except:
        return None


ocr_space_file("/home/jaime/cosas/codigo/trabajo-minciencias/corpus/red/pdfs_recortes/periódico15_329[6-7].pdf")