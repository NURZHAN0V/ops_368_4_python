client_list = [
    [1, "Олег", "+7 993 565 45 78", "@olegnastyle"],
    [2, "Дмитрий", "+7 993 657 45 78", "@dima"],
    [3, "Владимир", "+7 993 897 45 78", "@vova"]
]

def client_read():
    print("Список клиентов:👯\n")
    for client in client_list:
        print(
            f"ID: {client[0]}\n"
            f"Имя: {client[1]}\n"
            f"Телефон: {client[2]}\n"
            f"Телеграм: {client[3]}\n"
        )

def client_add():
    print("Добавление клиента 👨‍👧\n")

    user_last_id = len(client_list) + 1
    user_name = input("Имя: ")
    user_phone = input("Номер телефона: ")
    user_telegram = input("Телеграм: ")

    for client in client_list:
        if client[2] == user_phone:
            print(f"{client[1]} уже есть в базе")
            return
      
    client_list.append([
        user_last_id,
        user_name,
        user_phone,
        user_telegram
    ])
    print(f"Клиент {user_name} был добавлен ✔️")

def client_remove():
    print("Удаление клиента 👤\n")
    user_id_remove = int(input("Введите ID клиента: "))
    user_name_remove = ""
    for client in client_list:
        if client[0] == user_id_remove:
            client_list.remove(client)
            user_name_remove = client[1]
            print(f"Клиент {user_name_remove} был удален ❌")