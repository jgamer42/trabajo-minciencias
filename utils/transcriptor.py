import os 
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def transcriptor(ruta,extension):
    autent = IAMAuthenticator()
    speech_text=SpeechToTextV1(authenticator= autent)
    speech_text.set_service_url()
    with open(ruta,"rb")as audio:
        data=speech_text.recognize(
        content_type = f"audio/{extension}",
        audio=audio,
        model="es-CO_BroadbandModel"  
        ).get_result()
    audio.close()
    return data["results"][0]["alternatives"][0]["transcript"]

#transcriptor("../pruebas/angela.ogg","ogg")
