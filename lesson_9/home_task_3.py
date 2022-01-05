import random


def generate(a, b):
    for _ in range(100):
        yield random.randint(a, b)


if __name__ == '__main__':
    print(f'List of numbers that were created as a result of the generator function: '
          f'\n{" ".join(map(str, generate((int(input("First number: "))), (int(input("Second number: "))))))}')
