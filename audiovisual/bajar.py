import pandas as pd 
from pytube import YouTube
import os 
SOURCE = pd.read_csv("extraible.csv")
def bajar(link):
    base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
    video = YouTube(link)
    try:
        descargable = video.streams.filter(type="audio",file_extension="webm")[0]
        descargable.download("./videos")
        nombre = descargable.title
        
    except:
        print(f"fallo {link}")
        nombre = None
    return nombre

#print(bajar(SOURCE.link))
#print(bajar("https://www.youtube.com/watch?v=B3PaNSkkEL0"))
