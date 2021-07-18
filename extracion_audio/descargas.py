import requests
import os
import time
import webbrowser
import pyautogui as pag
from lxml import html
from dotenv import load_dotenv

load_dotenv() 

def descargar(link,universidad):
    pasosIvoox = [(1734,410,3),(1933,649,4),(2525,532,1),(2525,532,1),(2944,22,1),(3103,860,1),(2154,19,1),(2154,19,1)] 
    pasosSoundcloud = [(2341,580,4),(2451,653,3),(2154,19,1),(3103,860,1)]
    if "uniminuto" in link:
        uniminutoradio(link)
    elif "ivoox" in link:
        bot(link,universidad,pasosIvoox)
    elif "soundcloud" in link:
        bot(link,universidad,pasosSoundcloud)
    else:
        print("caso no contemplado")

def uniminutoradio(link):
    root_path = os.getenv("rootpath")
    response = requests.get(link)
    raw_html = html.fromstring(response.text)
    try:
        link = raw_html.xpath("//audio/a/@href")[0]
    except:
        link = raw_html.xpath("//audio/@src")
    ruta = os.path.realpath(f"{root_path}/corpus/red/sonoro/uniminutoradio")
    os.chdir(ruta)
    os.system(f"wget {link}")
    os.chdir(root_path)

def bot(link,universidad,pasos):
    root_path = os.getenv("rootpath")
    webbrowser.open(link)
    time.sleep(3)
    i = 0
    while i < len(pasos):
        time.sleep(pasos[i][2])
        pag.click(pasos[i][0],pasos[i][1],1,0,"left")
        i = i + 1
    time.sleep(60)
    try:
        archivo = os.listdir(f"{root_path}/corpus/sonoro")[0]
        os.system(f"mv '{root_path}/corpus/sonoro/{archivo}' '{root_path}/corpus/red/sonoro/{universidad}/{archivo}'")
    except:
        print(f"fallo {link}")