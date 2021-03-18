import requests
from lxml import html
import os
def uniminutoradio(link):
    response = requests.get(link)
    raw_html = html.fromstring(response.text)
    try:
        link = raw_html.xpath("//audio/a/@href")[0]
    except:
        link = raw_html.xpath("//audio/@src")
    ruta = os.path.realpath(f"../corpus/red/sonoro/uniminutoradio")
    os.chdir(ruta)
    os.system(f"wget {link}")

def ivoox(link,universidad,nombre):
    aux = link.split("_")[2:4]
    codigo, extension = aux
    extension = extension.split(".")[0]
    nuevo_link = f"http://www.ivoox.com/listen_mn_{codigo}_{extension}.m4a?internal=HTML5"
    ruta = os.path.realpath(f"../corpus/red/sonoro/{universidad}")
    os.chdir(ruta)
    os.system(f"wget {nuevo_link}")

def soundcloud(link):
    pass
