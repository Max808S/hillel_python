# Пользователь вводит, отдельно, строку ‘string’` и один символ `char`.
# Необходимо выполнить поиск в строке `string` всех символов `char`.
# Для решения НУЖНО использовать только функцию `find()`(rfind()), операторы `if` и `for`(while)

user_text = input('Enter any text: ')
user_letter = input('Enter any letter you want to find: ')

start = -1
count = 0

while True:
    start = user_text.find(user_letter, start+1)
    if start == -1:
        break
    count += 1

print(f'Letter "{user_letter}" written: {count} times. ')
