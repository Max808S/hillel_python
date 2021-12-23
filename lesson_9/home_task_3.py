import random


def generator(a=int, b=int):
    num_list = [random.randint(a, b) for i in range(1, 100)]
    return num_list


user_number_1 = int(input("Write the first number: "))
user_number_2 = int(input("Write the second number: "))

res = generator(user_number_1, user_number_2)
# print(f'{res}')

print(f'List of numbers that were created as a result '
      f'applying a lambda function to each element: \n '
      f'{" ".join(map(str, res))}')
