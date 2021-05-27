from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def transcribir(video):
    base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
    authenticator = IAMAuthenticator('')
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url('')
    texto = ""
    with open(f"{base}audiovisual/videos/{video}","rb") as audio_file:  
        data = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/webm',
            model='es-MX_BroadbandModel').get_result()
    for elemento in data["results"]:
        texto = texto + elemento["alternatives"][0]["transcript"]
    return texto
