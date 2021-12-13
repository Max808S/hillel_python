import random


random_list = [random.randint(1, 9) for i in range(10)]
print(f'A random list of 10 numbers: {random_list}')

print(f'Different numbers in the list - {len(set(random_list))}: {set(random_list)}')
