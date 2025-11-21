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
def send_clients(message):
    client = message.text
    new_client = client[12:].split(',')

    client_add(new_client)
    bot.reply_to(message, "Клиент добавлен!")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
# status_auth = login()

# if status_auth:
#     print("Вы успешно вошли в программу!")
# else:
#     print("Логин или пароль неверный")

# while status_auth:
#     print(
#         "1 - посмотреть всех килентов\n"
#         "2 - добавить нового клиента\n"
#         "3 - удалить клиента из списка\n"
#         "4 - редактировать клиента из списка\n"
#     )
#     value = input("Вы: ")

#     if value == "1":
#         print() # пустая строка
#         client_read()
#         print() # пустая строка
#     elif value == "2":
#         print() # пустая строка
#         client_add()
#         print() # пустая строка
#     elif value == "3":
#         print() # пустая строка
#         client_remove()
#         print() # пустая строка
#     elif value == "4":
#         print() # пустая строка
#         client_edit()
#         print() # пустая строка
#     else:
#         print("Выход из программы 👋")
#         break


bot.infinity_polling()