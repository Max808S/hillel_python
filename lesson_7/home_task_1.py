import random

initial_list = [random.randint(1, 9) for a in range(10)]
unique = tuple([e for e in initial_list if initial_list.count(e) == 1])

print(f'A randomly generated list of numbers: {initial_list}')
print(f'Unique elements from list in reverse: {unique[::-1]} ---> {type(unique)}')
