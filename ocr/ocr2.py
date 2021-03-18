import requests


def ocr_space_file(filename, overlay=False, api_key='', language='spa'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'scale':True,
               'OCREngine':2
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    print(r.content.decode())
    #return r.content.decode()

ocr_space_file("prueba.png")