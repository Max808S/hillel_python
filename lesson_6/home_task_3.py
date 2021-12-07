import random

random_list_1 = [random.randint(1, 100) for a in range(10)]
random_list_2 = [random.randint(1, 100) for b in range(10)]

print(f'Hello ;)\nThe program generates two lists with random numbers: '
      f'\nList #1: {random_list_1}'
      f'\nList #2: {random_list_2}')

result = list(set(random_list_1) ^ set(random_list_2))
print(f'Unique numbers for two lists: {len(result)}')
