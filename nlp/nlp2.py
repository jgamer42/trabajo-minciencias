from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import requests
import json
file = open(f"../exports/tadeo.json")
data = json.load(file)
prueba = data[2]["contenido"]

clientId = "FREE_TRIAL_ACCOUNT"
clientSecret = "PUBLIC_SECRET"

fromLang = "es"
toLang = "en"
jsonBody = {
    'fromLang': fromLang,
    'toLang': toLang,
    'text': prueba
}

headers = {
    'X-WM-CLIENT-ID': clientId, 
    'X-WM-CLIENT-SECRET': clientSecret
}

r = requests.post('http://api.whatsmate.net/v1/translation/translate', 
    headers=headers,
    json=jsonBody)
print(data[10]["link"])
#print("Status code: " + str(r.status_code))
print(prueba,"\n")
print(str(r.content))
analyzer = SentimentIntensityAnalyzer()
a = analyzer.polarity_scores(str(r.content))
print(a)