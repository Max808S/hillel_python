import random

random_list = [random.randint(1, 9) for a in range(10)]

print(f'Hello! This is random generated list: {random_list}')

k = random.choice(random_list)  # random position  'k'
C = random.choice(random_list)  # random number  'C'
v = random.choice(random_list)  # random number at the end

print(f'Add number C = "{C}" at position k = "{k}" in the list '
      f'and add another random number "{v}" to the end of the list.')

for i in range(len(random_list) - 1, k, -1):
    random_list[i] = random_list[i - 1]
random_list[k] = C

random_list.append(v)

print(f'This is a modified list: {random_list}')



