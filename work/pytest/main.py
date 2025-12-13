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

    if len(clients) > 0:
        bot.reply_to(message, clients)
    else:
        bot.reply_to(message, "База пуста")

user_sessions = {
    "status": False,
    "manager_id": None,
    "name": "",
    "phone": "",
    "telegram": ""
}
@bot.message_handler(commands=['new_client'])
def add_client(message):
    user_sessions["status"] = True
    user_sessions["manager_id"] = message.from_user.id
    bot.reply_to(message, "Напиши имя клиента 🙏")

@bot.message_handler(func=lambda msg: user_sessions["status"] and msg.from_user.id == user_sessions["manager_id"])
def handle_client_input(message):
    print(
        "Вызов функции: "
        f"{user_sessions["name"]}, "
        f"{user_sessions["phone"]}, "
        f"{user_sessions["telegram"]}\n"
    )
    if user_sessions["name"] == "":
        user_sessions["name"] = message.text.strip()
        print(user_sessions["status"], user_sessions["manager_id"])
        bot.reply_to(message, "Напиши номер телефона 🙏")
    elif user_sessions["phone"] == "":
        user_sessions["phone"] = message.text.strip()
        bot.reply_to(message, "Напиши телеграм 🙏")
    elif user_sessions["telegram"] == "":
        user_sessions["telegram"] = message.text.strip()

        response = client_add(
            user_sessions["name"],
            user_sessions["phone"],
            user_sessions["telegram"]
        )

        if response:
            bot.reply_to(message, "Пользователь добавлен")
        else:
            bot.reply_to(message, "Такой пользователь уже есть")
        
        user_sessions = {
            "status": False,
            "manager_id": None,
            "name": "",
            "phone": "",
            "telegram": ""
        }


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, user_sessions)


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