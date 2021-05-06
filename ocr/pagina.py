import webbrowser
import pyautogui as pag
import time
import os
import random
import configparser

def descargar(link,nombre):
    print(f"\n {link} \n")
    config = configparser.ConfigParser()
    config.sections()
    #agregar ruta relativa
    config.read("/home/jaime/cosas/codigo/trabajo-minciencias/general.cfg")
    posiciones = config["pagina"]
    webbrowser.open("http://issuu.pdf-downloader.com/")
    dormir = random.choice([2,3,4,5,6,7,8,10])
    time.sleep(dormir)
    #click en el formulario para el link
    pag.click(int(posiciones["x_link"]),int(posiciones["y_link"]),1,0,"left")
    for texto in link.split("/"):
        pag.write(texto)
        pag.hotkey("shift","7")
    #click en descargar
    pag.click(int(posiciones["x_download_1"]),int(posiciones["y_download_1"]),1,0,"left")
    dormir = random.choice([5,6,7,8,9,10,11,12,13,14,15,20,25,30,35,40])
    time.sleep(dormir)
    #click en descargar en la segunda pagina
    pag.click(int(posiciones["x_download_2"]),int(posiciones["y_download_2"]),1,0,"left")
    dormir = random.choice([20,25,30,35,40,45,50,55,60,65,70])
    time.sleep(dormir)
    #cierra la pestaña
    pag.click(int(posiciones["x_cerrar"]),int(posiciones["y_cerrar"]),1,0,"left")
    #guardar la primera vez en el pop up 
    pag.click(int(posiciones["x_guardar_1"]),int(posiciones["y_guardar_1"]),1,0,"left")
    dormir = random.choice([1,2,3,4,5,6,7,8,9,10,15,20,25,30])
    time.sleep(dormir)
    #click en guardar en el gestor de carpetas
    pag.click(int(posiciones["x_guardar_2"]),int(posiciones["y_guardar_2"]),1,0,"left")
    dormir = random.choice([1,2,3,4,5,6,7,8,9,10,15,20,25,30])
    time.sleep(dormir)
    #cierra la pestaña
    pag.click(int(posiciones["x_cerrar"]),int(posiciones["y_cerrar"]),1,0,"left")
    time.sleep(2)
    try:
        rename(nombre)
    except:
        print(f"fallo {nombre}")
    dormir = random.choice([1,2,3,4,5,6,7,8,9,10,15,20,25,30])
    time.sleep(dormir)


def rename(nombre):
    base = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.realpath(f"{base}/pdfs/")
    os.chdir(ruta)
    os.rename("ISSUU PDF Downloader.pdf",f"{nombre}.pdf")
    os.chdir(base)
    dormir = random.choice([1,2,3,4,5])
    time.sleep(dormir)

#print(pag.position())