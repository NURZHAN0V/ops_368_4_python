class Client:
    def __init__(self, id, name, phone, telegram):
        self.id = id
        self.name = name
        self.phone = phone
        self.telegram = telegram

# пример: [1, "Олег", "+7 993 565 45 78", "@olegnastyle"]
client_list = []

# посмотреть всех клиентов
def client_read():
    print("Список клиентов:👯\n")
    clients = []
    for client in client_list:
        clients.append([
            f"ID: {client.id}\n"
            f"Имя: {client.name}\n"
            f"Телефон: {client.phone}\n"
            f"Телеграм: {client.telegram}\n"
        ])
    return clients

# добавить клиента
def client_add(new_client):
    print("Добавление клиента 👨‍👧\n")

    user_last_id = len(client_list) + 1
    user_name = input("Имя: ")
    user_phone = input("Номер телефона: ")
    user_telegram = input("Телеграм: ")

    for client in client_list:
        if client.phone == user_phone:
            print(f"{client.name} уже есть в базе")
            return

    client_list.append(Client(id = user_last_id,name = user_name,phone = user_phone,telegram = user_telegram))
    print(f"Клиент {user_name} был добавлен ✔️")

# удалить клиента
def client_remove():
    print("Удаление клиента 👤\n")
    user_id_remove = int(input("Введите ID клиента: "))
    user_name_remove = ""

    for client in client_list:
        if client.id == user_id_remove:
            client_list.remove(client)
            user_name_remove = client.name
            print(f"Клиент {user_name_remove} был удален ❌")
            return

    print("Такого клиента нет в базе")

# редактирование клиента
def client_edit():
    user = None
    user_id = int(input("Введите ID клиента: "))

    # проверяем на существование
    for client in client_list:
        if client.id == user_id:
            user = client
            break

    if user:
        print(
            "1 - изменить имя\n"
            "2 - изменить номер телефона\n"
            "3 - изменить телеграм\n"
        )
        value = input("Вы: ")
        print() # пустая строка
        if value == "1":
            user.name = input("Имя: ")
        elif value == "2":
            user.phone = input("Телефон: ")
        elif value == "3":
            user.telegram = input("Телеграм: ")
        else:
            print("Команда не распознана 🤖")
            print("Попробуйте еще раз\n")
    else:
        print("Такого клиента нет в базе")