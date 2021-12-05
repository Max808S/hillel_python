welcome_text = 'Hello :)'
print(welcome_text)

user_number = int(input("Enter any natural number: "))
a = [int(i) for i in str(user_number)]


def check(num):
    for x in range(0, len(num) - 1):
        if num[x] == num[x + 1]:
            return False
    return True


if check(a):
    print("NO")
else:
    print("YES")
