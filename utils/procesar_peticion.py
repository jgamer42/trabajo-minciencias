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
    if datos.status_code != 200:
        return []
    try:
        post = datos.json().get("data")["posts"]
        for html_data in post:
            raw_data = html.fromstring(html_data)
            link = raw_data.xpath("//a[@href]/@href")[0]
            salida.append(link)
        return salida
    except:
        return []

def uniminuto(pagina,tdi,palabra):
    salida = []
    bandera = True
    url = "https://www.uniminutoradio.com.co/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=10.3.9.1"
    file = open("../../../utils/config_uniminuto.json")
    config = json.load(file)
    config["search_query"] = palabra
    config["class"] = tdi
    config["tdc_css_class"] = tdi
    config["tdc_css_class_style"] = tdi+"_rand_style"
    i = 0
    while i <= pagina:
        data = {
            "td_atts":str(config),
            "td_block_id":tdi,
            "td_column_number":2,
            "td_current_page":i,
            "block_type":"tdb_loop",
            "action" :"td_ajax_block",
            "td_magic_token" : "2b66e64254"
        }
        datos = requests.post(url, data=data)
        if datos.status_code != 200:
            break
        raw_data = datos.json().get("td_data")
        links = html.fromstring(raw_data)
        links = links.xpath("//div/a[@href]/@href")
        for link in links:
            if link.find("/seccion/") != -1:
                links.remove(link)
            salida.append(link)
        i += 1
    return salida
#uniminuto(37,"tdi_84_155","conflicto armado")
#print(eafit(1,10509,"0d23021",2791))
print(eafit(1,10509,"0d23021",2793))

