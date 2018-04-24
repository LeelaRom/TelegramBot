# -*- coding: utf-8 -*- 
'''
Created on 23 apr. 2018 �.

@author: leela
'''

import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

  
#Обработчик команды start    
@bot.message_handler(commands = ["start"])
def start(message):
    sent = bot.send_message(message.chat.id, "What is your name?")
    bot.register_next_step_handler(sent, hello)
    
    
def hello(message):
    bot.send_message(message.chat.id, "Hello, {name}, I am happy to see you.".format(mane=message.text))
    
    
if __name__ == '__main__':
    bot.polling(none_stop=True)