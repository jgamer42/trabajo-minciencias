import re 
import nltk 
from nltk.corpus import stopwords
from nltk.collocations import *
def tokenizar(texto):
    texto = texto.lower()

    plantilla = r"(?x)|(?:[A-Z]\.)+|\w+(?:-\w+)*|\$?\d+(?:\.\d+)?%?|\.\.\.|[][.,;\"\'?():-_\`]"
    salida = nltk.regexp_tokenize(texto,plantilla)
    salida = " ".join(salida)
    #salida = salida.split(" ")
    #for palabra in salida:
        #if palabra == " ''":
           # salida.remove(palabra)
    print(salida)
    return salida

def normalizar(texto):
    salida = []
    for palabra in salida:
        salida.append(palabra.strip())
    return texto

def limpiar_stop_words(texto):
    stops = stopwords.words("spanish")
    for word in texto:
        if word in stops:
            texto.remove(word)
        if word in ["en ","el ","la ","los","que","como","cada","de "," la"]:
            print(word)
            texto.remove(word)
    return texto

def riqueza_lexica(texto):
    vocabulario = sorted(set(texto))
    return len(vocabulario)/len(texto)

def palabra_mas_usada(texto):
    dist_frequencia = nltk.FreqDist(texto)
    return dist_frequencia.most_common(1)
    

def bi_gramas(texto): 
    salida = list(nltk.bigrams(texto))
    dist_frequencia = nltk.FreqDist(salida)
    return dist_frequencia.most_common(10)



a = tokenizar('''El puerto petrolero, con más de 300 mil habitantes, ha sido uno de los municipios más afectados por el conflicto armado en Santander. Actualmente, la   conserva un registro de 56.838 víctimas de desaparición forzada y homicidio. En Barrancabermeja han hecho presencia no solo grupos guerrilleros -Ejército de Liberación Nacional (Eln), Fuerzas Armadas Revolucionarias de Colombia (Farc – EP), Ejército Popular de Liberación (EPL)-, sino además grupos de autodefensas como el Bloque Central Bolívar. Una de las masacres del puerto petrolero, ocurrió el 16 de mayo de 1998, un hecho perpetrado bajo las órdenes Guillermo Cristancho Acosta conocido con el alias de ‘Camilo Morantes’, jefe de las Autodefensas de Santander, en el que aproximadamente 30 hombres armados, vestidos de civil, llegaron al barrio El Campín hacia  las 9:30 de la noche y retuvieron a 32 personas, quienes después fueron asesinadas. Brandon Esteban Escobar Ríos ha sido una de las víctimas que ha dejado la época de conflicto en el municipio. El joven de 17 años creció sin su padre, debido a que este fue secuestrado el 25 de julio de 2001, por un grupo de paramilitares. Durante unos días fue dado como desaparecido por sus familiares. Las últimas personas en verlo con vida fueron los dueños de un establecimiento, quienes contaron que unos sujetos se habían llevado a un grupo de hombres que estaba en el lugar. Escobar Ríos comentó que tres días después, el 28 de julio, luego de una intensa búsqueda, su familia se enteró que los restos de su padre habían sido vistos flotando en el río Magdalena. El hombre había sido descuartizado.  “Yo crecí sin mi papá y eso me afectó como a cualquier persona. Me crié solo porque mi mamá siempre estaba trabajando para que no me faltara nada. Ellos me quitaron la oportunidad de poder vivir con él”, afirmó el joven. Este es un espacio creado por la Universidad de la Paz (Unipaz) que tiene como propósito formar cultura de perdón a los habitantes de la región. El OCP está conformado por un equipo de docentes y alumnos de dicha universidad, quienes por medio de la memoria histórica, la justicia transicional y el perdón buscan establecer mecanismos que ayuden a la construcción de paz. 
Este grupo maneja tres líneas de trabajo: Construcción de territorio; cultura y ciudadanía; y conflicto, posconflicto y paz.  Bajo estos ejes se involucra a la comunidad estudiantil para que realice investigaciones por medio de semilleros. En el OCP estudian la situación de los derechos humanos, la democracia y la participación de la ciudadanía en las políticas públicas. Para Darío Monsalve Gómez, docente de la Unipaz e integrante del OCP, este espacio es un “referente en el que se reflejan las iniciativas de paz y las condiciones dadas para la convivencia y el diálogo en Barrancabermeja y el Magdalena Medio”. Durante  2015 desarrollaron como actividades dos sesiones con el Concejo Municipal de Barrancabermeja, alianzas con el Programa de Desarrollo y Paz del Magdalena Medio y una jornada de sensibilización en resolución de conflictos llamada “Va jugando”, entre otros proyectos de investigación que fueron adelantados por estudiantes universitarios. Además, han logrado alianzas con otras organizaciones lo que les ha permitido hacer seminarios y foros.  Para Monsalve Gómez, cada día se refleja mayor participación de los estudiantes en los ejercicios de pedagogía que han realizado. Sin embargo, comentó que es importante que cada día se vinculen más personas, porque el “OCP facilita los escenarios para la construcción de la paz y la convivencia, y proyecta además el futuro sobre el que se cimentará el posconflicto”, manifestó. Juan Carlos Peña Martínez es un alumno de dicha universidad y participante del observatorio, para quien el OCP es una forma de estudiar y visibilizar a aquellas comunidades del Magdalena Medio que en medio de la guerra han propuesto otras formas de vida. Más de 40 jóvenes se reunieron en la sede de las instalaciones de la Unión Sindical Obrera, USO, el pasado 17 de agosto. Los participantes fueron estudiantes de primer semestre de comunicación social de la Unipaz y los alumnos de bachillerato de los colegios Intecoba, Escuela Normal Cristo Rey y el Instituto Técnico Superior Industrial. Este espacio contó con la participación del OCP y estuvo orientado a una reflexión sobre la paz. También resaltaron la opinión que tienen los jóvenes frente a este tema. Durante el evento realizaron un debate en el que trataron temas referentes a las negociaciones que se adelantaron en La Habana, Cuba, entre el Gobierno Nacional y las Farc y resolvieron las dudas que tenían los estudiantes frente a los aspectos clave del acuerdo. Para Dario Monsalve Gómez la importancia de la participación del OCP, en la Tertulia de paz y Región, radica en que fue fundamental para “orientar parte del evento y transmitir a los jóvenes asistentes información sobre convivencia, ciudadanía y diálogo, teniendo en cuenta además el actual proceso de paz”, expresó el docente. Las conclusiones reunidas sobre esta actividad las tendrán en cuenta para integrarlas al próximo seminario, que se realizará en octubre de este año, y que tendrá como temática principal Ciudad, Región, Paz y Comunicación social. Según un documento  del Movimiento Nacional de Víctimas de Crímenes de Estado, en Barrancabermeja los principales responsables de los asesinatos cometidos entre 1988 y 1993, fueron los grupos paramilitares. Las víctimas eran especialmente residentes de los barrios populares, específicamente, los de las comunas 6 y 7.
''')
#a = normalizar(a)
#limpia = limpiar_stop_words(a)
#a = bi_gramas(limpia)
#print(a)