from clients import *

while True:
    print(
        "1 - посмотреть всех килентов\n"
        "2 - добавить нового клиента\n"
        "3 - удалить клиента из списка\n"
    )
    value = input("Вы: ")

    if value == "1":
        print() # пустая строка
        client_read()
        print() # пустая строка
    elif value == "2":
        print() # пустая строка
        client_add()
        print() # пустая строка
    elif value == "3":
        print() # пустая строка
        client_remove()
        print() # пустая строка
    else:
        break