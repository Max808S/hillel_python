import random


def generate(value=None):
    for _ in range(100):
        yield random.randint(1, 100)


if __name__ == '__main__':
    print(f'List of numbers that were created as a result '
          f'of the generator function: \n{" ".join(map(str, generate()))}')
