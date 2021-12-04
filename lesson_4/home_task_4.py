# Написать программу которая запрашивает у пользователя два слова через пробел.
# Определить что введено именно 2 слова - если нет то запросить ввести то что требуется еще раз.
# Программа печатет слова в порядке следования, но они должны быть перевернутые и каждое слово
# должно начинаться с заглавного символа а все остатльные были приведены к нижнему регистру.

welcome_text = 'Hello :)'
print(welcome_text)

while type(welcome_text) == str:
    text = input('Enter any 2 words: ')
    text_list = text.split()

    if 1 < len(text_list) < 3:
        a = text_list[0]
        b = text_list[1]

        c = a[::-1]
        d = b[::-1]
        print(c.capitalize(), d.title())
        break
    else:
        print('Only 2 words need to be written! Please try again: ')
