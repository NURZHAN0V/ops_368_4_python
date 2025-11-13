# Python 13-11-2025
## Инструкция по запуску программы

### Создали виртуальное окружение

```bash
python -m venv venv
```

### Дали разрешение на выполнения команд в терминале
Команда выполняется только первый раз, после создания виртуального окружения

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Активируем виртуальное окружение

```bash
venv\Scripts\Activate.ps1
```

### Запускаем приложение

```bash
python main.py
```

## MVP

### Создали список клиентов

```python
client_list = [
    ["Олег", "+7 993 565 45 78", "@olegnastyle"],
    ["Дмитрий", "+7 993 657 45 78", "@dima"],
    ["Владимир", "+7 993 897 45 78", "@vova"],
]
```

### Вывели список с клиентами

```python
print(client_list)
```

### Вывели килентов

```python
    for client in client_list:
        print(f"{count}. {client[0]}")
        count = count + 1
```

### Добавление клиентов

```python
client_list.append([
    input("Имя: "),
    input("Номер телефона: "),
    input("Телеграм: ")
])
```

### Написали рабочую программу

```python
while True:
    print(
        "1 - посмотреть всех килентов\n"
        "2 - добавить нового клиента\n"
        "3 - удалить клиента из списка\n"
    )
    value = input("Вы: ")
    
    # посмотреть всех клиентов
    if value == "1":
        print() # пустая строка
        count = 1
        for client in client_list:
            print(f"{count}. {client[0]}")
            count = count + 1
        print() # пустая строка

    # добавить нового клиента
    elif value == "2":
        print() # пустая строка
        client_list.append([
            input("Имя: "),
            input("Номер телефона: "),
            input("Телеграм: ")
        ])
        print() # пустая строка
```
