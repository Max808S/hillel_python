import random

comp_number = random.randint(1, 100)
user_number = -1
counter = 0

print('Hi :) You need to guess a number from 1 to 100')

while user_number != comp_number:
    counter += 1
    try:
        user_number = int(input('Enter any number: '))
    except ValueError:
        print('Bad input! Only numbers can be entered.')
        continue
    if user_number > 100:
        print(f'Sorry, your number {user_number} is larger than 100. Try again: ')
        continue
    elif user_number < 1:
        print(f'Sorry, your number {user_number} is less than 1. Try again: ')
        continue
    elif user_number > comp_number:
        print(f'Almost.. your number {user_number} bigger than hidden number. Try again: ')
        continue
    elif user_number < comp_number:
        print(f'Almost.. your number {user_number} lowest than hidden number. Try again: ')
        continue
    else:
        user_number == user_number
    print(f'Congrats! You guessed the number on {counter} attempts. Winner number {comp_number} :)')
