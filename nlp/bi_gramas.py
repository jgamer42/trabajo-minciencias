import re 
import nltk 
from nltk.corpus import stopwords
from nltk.collocations import *
import configparser

def extraer_bi_gramas(texto):
    salida = tokenizar(texto)
    i = 0
    while (i < 10):
        salida = limpiar_stop_words(salida)
        i = i + 1
    salida = bi_gramas(salida)
    return salida

def tokenizar(texto):
    texto = texto.lower()
    texto = texto.strip()
    plantilla = r"[\W\t\n]+"
    salida =re.split(plantilla,texto)
    for palabra in salida:
        if palabra in [" ",".",",",""]:
            salida.remove(palabra)
    return salida

def limpiar_stop_words(texto):
    config = configparser.ConfigParser()
    config.sections()
    config.read("/home/jaime/compartida/codigo/trabajo-minciencias/general.cfg")
    palabras = config["stop_words"]["palabras"]
    stops_personalizadas = palabras.split(",")
    stops = stopwords.words("spanish")
    for word in texto:
        if word in stops or word in stops_personalizadas or len(word) == 1:
            texto.remove(word)
    return texto

def bi_gramas(texto): 
    salida = list(nltk.bigrams(texto))
    dist_frequencia = nltk.FreqDist(salida)
    return dist_frequencia.most_common(50)

def extraer_colocaciones(texto):
    medida_bigramas = nltk.collocations.BigramAssocMeasures()
    buscador = BigramCollocationFinder.from_words(texto)
    #buscador.apply_freq_filter(3)
    return buscador.nbest(medida_bigramas.pmi,10)
a = tokenizar("En Colombia existen 7.7 millones de afectados porla violencia y el conflicto armado, de las cuales la mayoría han sido afectadas por grupos guerrilleros, paramilitares y bandas criminales, también se reporta un porcentaje significativo de ciudadanos a quienes la fuerza pública y el Estado les han violado parte de sus derechos. Algunas víctimas de la violencia sexual hacen parte de este grupo. La Red Nacional de Información (RNI) estima que al menos 13.598 personas han padecido delitos contra la libertad e integridad sexual. De ellas, 12.182 son mujeres (aproximadamente un 90% de los afectados); 1.067, hombres; y 71 personas con orientación sexual o identidad de género no hegemónica (comunidad Lgtbi). Para el caso de Santander, según la Unidad para la Atención y Reparación Integral a las Víctimas (Uariv), se cuenta con un registro de 353 víctimas reconocidas. La mayoría son mujeres. Patricia* es una de ella. No solo busca reparación integral por los hechos que narra a continuación. Asegura que las heridas dejadas por un arma de fuego no se comparan con las que una violación deja en la mente y el cuerpo de una persona. Víctimas de la violencia sexual, la otra cara del conflicto armado en la región El Periódico 15 conoció su historia. Alejada de su pasado y aún superando sus trágicas vivencias, hoy día integra el grupo de 25 mujeres que participan en los encuentros organizados en Bucaramanga por la Uariv de Santander conocidos como “Momentos”, con los cuales se busca “fortalecer la confianza en sí mismas y que exista un reconocimiento y acompañamiento para superar las dolorosas huellas del conflicto armado en su cuerpo”, aseguró Paula Gaviria Betancur, directora de la Unidad. Mientras pasea por su huerta y mira el paisaje, Patricia ubica dos sillas debajo de un árbol de mango para narrar su experiencia. Lo primero que cuenta es que proviene de una familia trabajadora que se asentó en el municipio de Piedecuesta hace más de 30 años. Allí terminó sus estudios como bachiller contable, en la misma época en la que su papá trabajaba como soldador industrial de profesión en el corregimiento de San Rafael de Lebrija, del municipio de Rionegro, Santander, y en la que decidió que toda la familia se debía trasladar allí, pero la joven se quedó. Pasados algunos meses Patricia se enamoró y quedó embarazada. Esto la llevó a dedicarse a su hogar y no pensar en un trabajo distinto que edificar su nuevo hogar. Cuando se aproximaba la fecha del nacimiento de su hija, ella optó por trasladarse a la tierra donde habitaban sus padres. Fue allí donde conoció por primera vez la violencia que vivía la Colombia de los años 90. Cuenta que mientras conversaba con un amigo en el andén de su casa, de repente se fue la luz; segundos después, hombres armados se acercaron a ese lugar, donde luego de un cruce de palabras entre ellos sobre la integridad de la joven embarazada, optaron por abrir la puerta de su casa y empujarla hacia adentro, para después acribillar a su compañero de charla. Ella, en estado de shock, se levantó de aquel lugar y corrió hacia el cuerpo que yacía tirado en un charco de sangre. Patricia no lo podía creer, agarró el cuerpo de su amigo y lo recostó, momento exacto en el que llegó la luz, no solo para dar claridad al pueblo, sino también para mostrar la realidad de este hecho violento, que hasta el momento no se lograba comprender por causa de la conmoción que visitaba a las personas del sector. Recuerda que su padre, al verla bañada en sangre, corrió y le desgarró la ropa para cubrir las heridas en su cuerpo, pero por fortuna estaba ilesa. La alegría que le produjo la llegada de su hija dejó de lado aquel fatídico momento. La niña nació y creció con una alegría y espontaneidad que la caracterizaba como una persona llena de sueños e ilusiones. Se alejaron de Rionegro y se radicaron en Arauca, donde madre e hija transitaban diariamente las decenas de hectáreas de cultivos de arroz. Mientras tanto, la región de Santander donde vivían sus padres era invadida por grupos paramilitares que atrozmente asesinaban y luego desmembraban los cuerpos de sus víctimas. Este flagelo visitó a una familia cercana a su hogar, dos de sus integrantes habían sido descuartizados. La noticia asombró y alarmó a Patricia, y pensó en la integridad de sus padres y hermanos. Este grupo armado ilegal conoció de la existencia de un soldador industrial en la zona, persona que podía servirles para el rompimiento del oleoducto de petróleo que pasaban por aquel lugar, negocio que era rentable para financiar sus delitos. Infortunadamente este soldador era el padre de Patricia, quien se negó a realizar aquellos trabajos. Esto desató la ira en su contra al no realizar dichos favores. Una noche, mientras esposos e hijos dormían, hombres armados llegaron a exigir la realización del trabajo. Asustados por las amenazas, guardaron silencio. Los paramilitares pensaron que la casa estaba sola, se montaron a un tractor, tumbaron el portón y rompieron la pared. De esa forma les dieron a conocer su descontento por no colaborar en lo que les pedían. Al conocer lo ocurrido, Patricia, con cuatro meses de embarazo de su segundo hijo, con una niña de 5 años y su chofer, decidió volver al lado de sus seres queridos. En el lugar tomó la camioneta de su propiedad, con la intención de ir a rescatar algunos de los enseres y maquinarias de trabajo de su padre. Después de lograr su objetivo, regresó a Arauca no solo en compañía de su niña y su chofer, sino también la de su hermano. En su viaje a Arauca, se detuvieron en Saravena con la intención de retirar algún dinero del cajero para poder hospedarse en un hotel y continuar el viaje al otro día. La tarjeta de crédito no funcionó. Pidieron colaboración en un hotel de la zona con la condición de que al otro día pagarían, pero el administrador no aceptó hospedarlos. A partir de este momento, debajo del follaje del árbol de mango y teniendo como panorámica el municipio de Piedecuesta, la actitud de Patricia cambió. Al parecer, los recuerdos le bombardeaban la mente y los sentimientos de dolor empezaron a relucir. Sin embargo, retomó la historia de Saravena. Recordó que en el municipio de Arauquita, a 58 kilómetros de aquel lugar, vivía una amiga de la familia que podía darles hospedaje. “Fue la peor decisión de mi vida”, expresó con un dolor notable en su rostro. Partieron a las 8:00 de la noche cuando de repente se encontraron un retén militar. “Necesitamos que lleven a dos soldados hasta allí adelante”, afirmó uno de los soldados. Patricia respondió: “no podemos llevarlos, mire que vamos llenos y no tenemos donde acomodarlos”. Después de un cruce de palabras, la Fuerza Pública permitió que continuara su camino. Pensando los ocupantes del vehículo que ya todo había pasado, una barricada estaba preparada metros más adelante, lo cual provocó de nuevo la detención del carro. “Tienen que llevarlos”, ordenaron los soldados. De esta manera y prácticamente obligados embarcaron como pudieron a los dos hombres en la camioneta. Dos kilómetros más adelante, uno de los uniformados mandó a detener el carro y se escuchó a uno de ellos decir: “Váyanse ustedes, pero la señora y la niña se quedan con nosotros”. Los hombres que viajaban con esta mujer reaccionaron negativamente a esta petición, palabras de todo tipo se cruzaban entre los civiles y los militares. Finalmente, sin entender nada de lo que estaban viviendo, recapacitó y dijo: “váyanse ustedes, yo me quedo sola, pero mi hija también se va”, petición que no fue aceptada por los miembros del ejército. Después de un forcejeo y de algunos golpes al tío de la niña, la mujer y su hija tuvieron que quedarse. Fueron llevadas a una construcción que se levantaba al lado de la carretera. Uno de los militares, de piel blanca como lo describe Patricia, le gritó, insinuándole que por ser una guerrillera era que estaba allí.")
b = limpiar_stop_words(a)
c = limpiar_stop_words(b)
d = limpiar_stop_words(c)
e = limpiar_stop_words(d)
ejemplo = bi_gramas(d)
print(ejemplo)
print(extraer_colocaciones(e))

