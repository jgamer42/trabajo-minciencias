import requests
from lxml import html
import json

def eafit(pagina,post_id,model_id,category):
    url = "http://bitacora.eafit.edu.co/wp-admin/admin-ajax.php"
    data = {
        "action": "raven_get_render_posts",
        "post_id": post_id,
        "model_id": model_id,
        "paged": pagina,
        "category": category,
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
