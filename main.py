from config import *  # importamos el token
import telebot # importamos el bot
import time
import threading

bot = telebot.TeleBot(TELEGRAM_TOKEN) # creamos el bot (instancia)

# creamos una funcion para que el bot responda a los comandos
@bot.message_handler(commands=['start','start2']) # definimos el comando
def start(message):
    """Da la bienvenida al usuario del bot"""
    bot.reply_to(message, 'Hola, soy un bot de prueba')
    print(message.chat.id)
    
    
@bot.message_handler(commands=['inicio']) # definimos el comando
def inicio(message):
    bot.send_message(message.chat.id, 'Este bot es una prueba')


@bot.message_handler(content_types=['new_chat_members'])
def new_chat_members(message):
    """Funcion que se ejecuta cuando un usuario entra en el grupo"""
    bot.reply_to(message, 'Bienvenido a la comunidad')    
    
# responde a los mensajes de texto que no son comandos
# text, audio, document, photo, sticker, video, voice, location, 
# contact, venue, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, 
# delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, 
# migrate_to_chat_id, migrate_from_chat_id, pinned_message
@bot.message_handler(content_types=['text'])
def bot_mensajes_texto(message):
    """Gestiona los mensajes de texto recibidos"""
    if message.text.startswith('/'):
        bot.send_message(message.chat.id, 'Chinga tu madre')
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        archivo = open('./docs/Doc.pdf', 'rb')
        bot.send_document(message.chat.id, archivo, caption="<b>DOCUMENTO</b>", parse_mode='HTML')


def recibe_mensajes():
    """Bucle que comprueba si hay mensajes nuevos"""
    bot.infinity_polling()
    
    
if __name__ == '__main__':
    print('Bot iniciado')
    hilo_bot = threading.Thread(name='hilo_bot', target=recibe_mensajes)
    hilo_bot.start()
    print('Fin')
# Escribe lo que esta haciendo el bot (...Escribiendo)
# bot.send_chat_action(message.chat.id, 'typing')


# Enviar video
# video = open('./video/Intro.mp4', 'rb')
# bot.send_document(message.chat.id, video, caption="<b>VIDEO</b>", parse_mode='HTML')  


# Enviar documento
# archivo = open('./docs/Doc.pdf', 'rb')
# bot.send_document(message.chat.id, archivo, caption="<b>DOCUMENTO</b>", parse_mode='HTML')  
  
    
# Enviar imagenes    
# foto = open('./images/Listo.jpg', 'rb')
# bot.send_photo(message.chat.id, foto, "<b>IMAGEN</b>", parse_mode='HTML')   
   
    
# Para borrar el mensaje del usuario
# bot.delete_message(message.chat.id, message.message_id)   
   
    
# Eliminar un mensaje despues de 3 segundos    
# x = bot.send_message(message.chat.id, '<b>Hola</b>', parse_mode='HTML')
# time.sleep(3)
# bot.delete_message(message.chat.id, x.message_id)    
    
    
# Editar un mensaje despues de 3 segundos
# x = bot.send_message(message.chat.id, '<b>Hola</b>', parse_mode='HTML')
# time.sleep(3)
# bot.edit_message_text('<b>Adiós</b>', message.chat.id, x.message_id, parse_mode='HTML')


# Enviar texto formateado
# texto_html = '<b>Negrita</b>, <i>cursiva</i>, <a href="http://google.com">link</a>' + '\n'
# texto_html += '<span class="tg-spoiler">Spoiler</span>'
# bot.send_message(message.chat.id, texto_html, parse_mode='HTML')