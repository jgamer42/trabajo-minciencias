import requests
from lxml import html
import json

def procesar_peticion(pagina):
    url = "http://bitacora.eafit.edu.co/wp-admin/admin-ajax.php"
    data = {
        "action": "raven_get_render_posts",
        "post_id": 10509,
        "model_id": "637a27c",
        "paged": pagina,
        "category": -1,
    }
    salida = []
    datos = requests.post(url, data=data)
    post = json.loads(datos.text)
    post = post["data"]["posts"]
    for html_data in post:
        raw_data = html.fromstring(html_data)
        link = raw_data.xpath("//a[@href]/@href")[0]
        salida.append(link)
    return salida
