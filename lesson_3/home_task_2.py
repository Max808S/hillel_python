# Как поменять значения 2х переменных местами не используя третей переменной и не используя свойст
# множественного присваивания ? Если известно что числа в переменных целочисленные.

a = 5
b = 10

a = a * b
b = a / b
a = a / b

print(a)
print(b)
