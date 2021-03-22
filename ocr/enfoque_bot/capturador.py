import webbrowser
import pyautogui
import pyautogui as pag
import time
def capturar(paginas,link,nombre):
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
    pag.click(1140,742,1,0,"left")
    pag.moveTo(1142,600)
    time.sleep(10)
    complemento=''
    if paginas[0]%2==0:
        complemento = f"{paginas[0]}-{paginas[0]+1}"
    else:
        complemento = f"{paginas[0]-1}-{paginas[0]}"
    nombre_imagen_salida = f"{nombre}_{complemento}.jpg"
    pyautogui.screenshot(nombre_imagen_salida)
    pyautogui.screenshot(nombre_imagen_salida)
    if len(paginas) >= 2:
        if paginas[0]%2 == 0:
            pass
        else:
            complemento = f"{paginas[1]}-{paginas[1]+1}"
            nombre_imagen_salida = f"{nombre}_{complemento}.jpg"
            pag.click(1324,378,1,0,"left")
            time.sleep(2)
            pag.click(1140,742,1,0,"left")
            pag.moveTo(1142,600)
            time.sleep(10)
            pyautogui.screenshot(nombre_imagen_salida)



