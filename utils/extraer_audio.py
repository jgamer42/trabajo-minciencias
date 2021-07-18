from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def transcribir(video):
    base = "/home/jaime/cosas/codigo/trabajo-minciencias/"
    authenticator = IAMAuthenticator('Ivh3xZHx-oKvhBoSoW4ZeKi698_5kMrfBSSnhoOmNGpz')
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/e4aa84d3-1794-41a2-951f-9953da3ae638')
    texto = ""
    with open(f"{base}audiovisual/videos/{video}","rb") as audio_file:  
        data = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/webm',
            model='es-MX_BroadbandModel').get_result()
    for elemento in data["results"]:
        texto = texto + elemento["alternatives"][0]["transcript"]
    return texto
