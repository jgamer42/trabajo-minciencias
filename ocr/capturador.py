import webbrowser
import pyautogui
import pyautogui as pag
import time
from prepros import recortar
def capturar(paginas,link):
    webbrowser.open(link)
    time.sleep(15)
    #f_screen
    pag.click(943,748,1,0,"left")
    #next
    pag.click(1324,378,1,0,"left")
    #pag_inicial/2
    pag.click(1324,378,int(paginas[0]/2)-1,0,"left")
    #zoom
    time.sleep(1)
    pag.click(1137,742,1,0,"left")
    time.sleep(5)
    pyautogui.screenshot("salida.jpg",region=(218,39,1107,703))
    recortar("salida.jpg")
    if len(paginas) >= 2:
        if paginas[0]%2 == 0:
            pass
        else:
            pag.click(1324,378,1,0,"left")
            #time.sleep(1)
            #pag.click(1137,742,1,0,"left")
            time.sleep(5)
            pyautogui.screenshot("salida2.jpg",region=(331,106,860,577))
            recortar("salida2.jpg")
capturar([17,18],"https://issuu.com/dateatealminuto/docs/dateate_edicion_45_v6_impresion")    
#print(pag.position())

