welcome_text = "Hello :)"
print(welcome_text)

while welcome_text:
    user_number = int(input('Enter any number from 3 to 9: '))
    if 2 < user_number < 10:
        for i in range(1, user_number + 1):
            left = ''.join(map(str, range(1, i)))
            print(f'{left}{i}{left[::-1]}')
        break
    else:
        print('A number is out of range. Try again: ')
