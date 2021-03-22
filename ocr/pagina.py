import webbrowser
import pyautogui as pag
import time
import os
def descargar(link,nombre):
    webbrowser.open("http://issuu.pdf-downloader.com/")
    time.sleep(3)
    pag.click(513,432,1,0,"left")
    for texto in link.split("/"):
        pag.write(texto)
        pag.hotkey("shift","7")
    pag.click(706,493,1,0,"left")
    time.sleep(20)
    pag.click(703,280,1,0,"left")
    time.sleep(5)
    pag.click(1148,710,1,0,"left")
    time.sleep(2)
    pag.click(1280,58,1,0,"left")
    time.sleep(5)
    rename(nombre)

def rename(nombre):
    base = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.realpath(f"{base}/pdfs/")
    os.chdir(ruta)
    os.rename("ISSUU PDF Downloader.pdf",f"{nombre}.pdf")
    os.chdir(base)



