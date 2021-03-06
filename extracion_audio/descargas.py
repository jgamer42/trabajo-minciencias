import requests
from lxml import html
import os
def uniminutoradio(link):
    response = requests.get(link)
    raw_html = html.fromstring(response.text)
    link = raw_html.xpath("//audio/a/@href")[0]
    ruta = os.path.realpath(f"../corpus/red/sonoro/uniminutoradio")
    os.chdir(ruta)
    os.system(f"wget {link}")

def ivoox(link,universidad):
    audio = link.split("_")[2]
    ruta = os.path.realpath(f"../corpus/red/sonoro/{universidad}")
    os.chdir(ruta)
    os.system(f"wget {audio}")