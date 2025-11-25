from clients import *
from auth import *
from config import *
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, это CRM для учета клиентов! Чтобы добавить пользователя напиши: `/new_client Олег,+7 993 907 98 29,@olegnastyle`")

@bot.message_handler(commands=['clients'])
def send_clients(message):
    clients = client_read()
    for client in clients:
        bot.reply_to(message, client)

# `/new_client Олег,+7 993 907 98 29,@olegnastyle`
@bot.message_handler(commands=['new_client'])
def send_client(message):
    client = message.text
    new_client = client[12:].split(',')

    client_add(new_client)
    bot.reply_to(message, "Клиент добавлен!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()