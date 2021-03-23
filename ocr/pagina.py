import webbrowser
import pyautogui as pag
import time
import os
import random
def descargar(link,nombre):
    webbrowser.open("http://issuu.pdf-downloader.com/")
    dormir = random.choice([2,3,4,5])
    time.sleep(dormir)
    pag.click(513,432,1,0,"left")
    for texto in link.split("/"):
        pag.write(texto)
        pag.hotkey("shift","7")
    pag.click(706,493,1,0,"left")
    dormir = random.choice([5,10,15,20,25])
    time.sleep(dormir)
    pag.click(703,280,1,0,"left")
    dormir = random.choice([20,25,30,35,40,45,50])
    time.sleep(dormir)
    pag.click(1148,710,1,0,"left")
    dormir = random.choice([1,2,3,4,5,6,7,8,9,10])
    time.sleep(dormir)
    pag.click(1280,58,1,0,"left")
    time.sleep(2)
    try:
        rename(nombre)
    except:
        print(f"fallo {nombre}")

def rename(nombre):
    base = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.realpath(f"{base}/pdfs/")
    os.chdir(ruta)
    os.rename("ISSUU PDF Downloader.pdf",f"{nombre}.pdf")
    os.chdir(base)



