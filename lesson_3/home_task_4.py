a = input("Введите натуральное число: ")

if a.isdigit() == True:
    n = 0
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] == a[j]):
                n+=1
    if n == 0:
        print('Нет.')
    else:
        print('Да.')
else:
    print("Это не натуральное число")