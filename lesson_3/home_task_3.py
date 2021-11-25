year = int(input("Введите год: "))


def leap() -> object:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год невысокосный")
    else:
        print("Год высокосный")


if 1900 < year < 1000000:
    leap()
else:
    print("Год не соответсвует условию")
