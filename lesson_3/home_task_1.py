# Написать програму для проверки пароля .
# У пользователя запрашивается пароль сравнивается с ожидаемой фразой -
# нужно сообщить о том что пароль совпал или пароль не совпал.

password = "123s"

password2 = input("Please enter password: ")

if password == password2:
    print("Welcome back")
elif password != password2:
    print("Wrong password")

