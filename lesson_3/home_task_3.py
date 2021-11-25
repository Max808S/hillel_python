year = int(input("Введите год: "))

if 1900 < year < 1000000:
    print("Год не высокосный" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Год высокосный")
else:
    print("Год не соответсвует условию")
