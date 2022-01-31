def write_string():
    try:
        with open('data_ht_1.txt', 'w', encoding='utf-8') as a:
            while True:
                user_input = input('Write any text. To finish type enter: ')
                if user_input == '':
                    print(f'Entry added.')
                    break
                a.write(user_input + "\n")
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    write_string()
