import random


def check_list(test_list=[], test_number=''):
    for x in test_list:
        for y in test_list:
            if x + y == test_number:
                return test_list.index(x), test_list.index(y)


list_1 = [random.randint(0, 9) for i in range(10)]
list_2 = [random.randint(0, 9) for i in range(10)]

number_1 = random.randint(5, 20)
number_2 = random.randint(5, 20)

print(f'Hello! Generated two lists of random numbers: \n'
      f'List #1: {list_1} \nList #2: {list_2} \n'
      f'and two random numbers for each list: #1 = {number_1}, #2 = {number_2}')

check_list_1 = check_list(list_1, number_1)
check_list_2 = check_list(list_2, number_2)

print(f'In the first list index of numbers, the sum of which is {number_1}: {check_list_1} \n'
      f'in the second list index of numbers, the sum of which is {number_2}: {check_list_2}.')

