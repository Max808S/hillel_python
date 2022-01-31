def main():
    try:
        with open('article.txt', 'r', encoding='utf-8') as file1:
            print(f'Longest word: {longest_words(file1)}')
    except Exception as ex:
        print(ex)


def longest_words(file):
    try:
        all_words = file.read().split()
        the_longest = []
        length_max = len(max(all_words, key=len))
        for x in range(len(all_words)):
            if length_max == len(all_words[x]):
                the_longest.append(all_words[x])
        if len(the_longest) == 1:
            for i in the_longest:
                return i
        elif len(the_longest) > 1:
            return the_longest
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()