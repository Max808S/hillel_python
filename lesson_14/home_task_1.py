def test_exception():
    value_a = input('Enter the first value: ')
    value_b = input('Enter the second value: ')
    try:
        res_string = int(value_a) + int(value_b)
        return res_string
    except ValueError:
        res_integer = str(value_a) + str(value_b)
        return res_integer


if __name__ == "__main__":
    print(test_exception())
