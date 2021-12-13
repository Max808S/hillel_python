import random


list_1 = [random.randint(0, 9) for a in range(14)]
list_2 = [random.randint(0, 9) for b in range(14)]

res = set(list_1).intersection(set(list_2))

print(f'First generated list: {list_1}'
      f'\nSecond generated list: {list_2}')

print(f'Same numbers in two lists - {len(res)}: {res}')
