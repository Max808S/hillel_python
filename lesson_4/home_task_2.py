welcome_text = 'Hello :)'
print(welcome_text)

user_number = int(input('Enter any natural number: '))


def check(a):
    number = int(a) ** 2
    return True if str(number)[-len(a):] == a else False


for i in range(1, user_number + 1):
    if check(str(i)):
        print(f'{i}*{i}={i * i}')

print('Easy math :)')
