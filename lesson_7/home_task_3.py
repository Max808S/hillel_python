dictionary = {}
for key in input('Write a sentence: ').split():
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] += 1
for key, count in dictionary.items():
    print(f"The word {key} is repeated {count} times.")
