welcome_text = 'Hello :)'
print(welcome_text)


def check(num):
    return "YES" if any(num.count(i) > 1 for i in num) else "NO"


user_number = input('Enter any natural number: ')
print(check(user_number))
