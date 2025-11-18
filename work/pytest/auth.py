login_admin = "admin"
password_admin = "admin"

def login():
    login = input("Логин: ")
    password = input("Пароль: ")

    if login_admin == login and password_admin == password:
        return True
    else:
        False