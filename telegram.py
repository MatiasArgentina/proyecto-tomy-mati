"""
Ejemplo 1 - Este programa escribe por Terminal el contenido del ultimo mensaje
            que ha recibido el chatbot junto con el nombre del autor y la ID del chat.
"""
 
#Importar librerias
import json
import requests
import time

#Variables para el Token y la URL del chatbot
TOKEN = "1359378146:AAE9wce12SiRlRALbV2JZTDR7XTWM6W34NY" 
URL = "https://api.telegram.org/bot" + TOKEN + "/"

Users = [['Matias','1061454232'], ['Tbomb','1384358984']]

def update():
    #Llamar al metodo getUpdates del bot haciendo una peticion HTTPS (se obtiene una respuesta codificada)
    respuesta = requests.get(URL + "getUpdates") 
    #Decodificar la respuesta recibida a formato UTF8 (se obtiene un string JSON)
    mensajes_js = respuesta.content.decode("utf8")
    #Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)
    #Devolver este diccionario
    return mensajes_diccionario
  
def leer_mensaje():
 
    #Llamar update() y guardar el diccionario con los mensajes recientes
    mensajes = update()
    #Calcular el indice del ultimo mensaje recibido
    indice = len(mensajes["result"])-1
    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensajes["result"][indice]["message"]["text"]
    persona = mensajes["result"][indice]["message"]["from"]["first_name"]
    id_chat = mensajes["result"][indice]["message"]["chat"]["id"]
 
    #Mostrar esta informacion por pantalla
    print(persona + " (id: " + str(id_chat) + ") ha escrito: " + texto)
 
#Llamar a la funcion "leer_mensaje()"
leer_mensaje()

#Escribir
def enviar_mensaje(idchat, texto):
    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))

for User in Users:
    text = "Hola " +User[0] + " son las: "+time.strftime("%H:%M:%S")
    enviar_mensaje(User[1], text)