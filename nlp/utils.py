import nltk 
from nltk.collocations import *

def riqueza_lexica(texto):
    vocabulario = sorted(set(texto))
    return len(vocabulario)/len(texto)

def palabra_mas_usada(texto):
    dist_frequencia = nltk.FreqDist(texto)
    return dist_frequencia.most_common(1)