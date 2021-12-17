from collections import Counter

text = """Стоишь на берегу и чувствуешь соленый запах ветра, что веет с моря, и веришь,
что свободен ты и жизнь лишь началась, и губы жжет подруги поцелуй, пропитанный слезой!"""

# printing original string
print(f'The original string: {text}')

# initializing split
split = ' '

# splitting using split()
temp = text.split(split)

text_dict = {}

# using loop to reform dictionary with splits
for index, element in enumerate(temp):
    text_dict[index] = element

# repeating elements in dictionary
true_res = Counter(text_dict.values())

print(f'Dictionary after line splitting: {text_dict}')
print(f'Result! The most frequent word in the text: {true_res.most_common(1)}')
