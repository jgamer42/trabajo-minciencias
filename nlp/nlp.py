import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from translate import Translator
analyzer = SentimentIntensityAnalyzer()
translator = Translator(from_lang="spanish",to_lang="english")
file = open(f"../exports/tadeo.json")
data = json.load(file)
prueba = data[0]["contenido"]
print(prueba+"\n")
traduccion = translator.translate(prueba)
print(traduccion)