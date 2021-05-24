import pandas as pd
from pytube import YouTube   
file = pd.read_csv("extraible.csv")
links = file.link
test = links[0]
yt = YouTube(test)
data = yt.streams.filter(type="audio")[0]
data.download()