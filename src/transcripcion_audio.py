import speech_recognition as spr
audio = "wpp.wav"
src = spr.Recognizer()
with spr.AudioFile(audio) as source:
    print(source)
    audio = src.listen(source)
    text = src.recognize_google(audio,language="es-ES")
    print(text)
    

