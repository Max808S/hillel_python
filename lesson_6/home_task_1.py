import random

random_list = [random.randint(1, 99) for a in range(10)]
k = random.choice(random_list)  # random number

print(f'Hello! This is random generated list: {random_list}'
      f'\nRandom number from the list: k - {k}')

random_list.remove(k)
random_list.pop()

print(f'WORK: Remove from the list the number {k} with index k '
      f'and remove the last element of the list')

print(f'Modified list: {random_list}')
