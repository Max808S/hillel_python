from time import time


def timer_func(func):
    """
    Function execution time
    """
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        total_time = (t2 - t1)
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        speed_res.append(total_time)
        return result

    return wrap_func


@timer_func
def linear_search_1(arr, search):
    """
    Line search function #1
    """
    for i in range(len(arr)):
        if arr[i] == search:
            return i
    print(f'\n\U00002733 Finding an item {search} in the first way \U00002935')
    return


@timer_func
def linear_search_2(arr, search):
    """
    Line search function #2
    """
    for val in enumerate(arr):
        if val[1] == search:
            return val[0]
    print(f'\n\U00002733 Finding an item {search} in the second way \U00002935')
    return None


@timer_func
def linear_search_3(arr, search):
    """
    Line search function #3
    """
    print(f'\n\U00002733 Searching for an item {search} in a third way \U00002935')
    return arr.index(search) if search in arr else None


print(f'Hello! Creating a list of natural numbers from 1 - 10,000,000 ')

test_list = list(range(1, 10000000))
speed_res = []

print(f'List created! We can find any number from a given range \U00002934')

true_id = 'Yes'
false_id = 'No'


def enter(access=''):
    """
    Function that start checks
    """
    while access != true_id and access != false_id:
        print('\U00002733 You can only write: "Yes" or "No"')
        return enter(input('\U00002733 Please try again: '))

    if access == true_id:
        print(f'\U00002733 The program will calculate the execution time of the functions...')
        target = input('\U00002733 Write a number from 1 to 10,000,000: ')

        linear_search_1(test_list, target)
        linear_search_2(test_list, target)
        linear_search_3(test_list, target)

        print(f'\nCheck completed \U00002705, fastest function speed ---> {(sorted(speed_res)[0]):.4f}s ')

    elif access == false_id:
        print('Good bye!')


enter(input('\U00002705 / \U0000274C Do you wanna test a functions for the speed of execution? (Yes/No): '))
