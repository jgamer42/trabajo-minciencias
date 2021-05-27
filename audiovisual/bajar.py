import pandas as pd 
from pytube import YouTube
SOURCE = pd.read_csv("extraible.csv")
def bajar(link):
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
print(bajar("https://www.youtube.com/watch?v=B3PaNSkkEL0"))
