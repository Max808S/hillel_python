import random


def get_matrix():
    """
    Generates a matrix with random numbers of the size entered by the user.
    Calculates the sum of each row and column.
    """
    m = int(input('Enter the number of strings: '))
    n = int(input('Enter the number of columns: '))
    matrix = [[random.randint(1, 50) for i in range(n)] for j in range(m)]
    column_sum = []

    print(f'Strings: {n}. Columns: {m}.\n')

    # calculate the sum of matrix strings
    for i in range(m):
        summa = 0
        for j in range(n):
            summa += matrix[i][j]
        matrix[i].append(summa)

    # calculate the sum of matrix columns
    for i in range(n):
        summa = 0
        for j in range(m):
            summa += matrix[j][i]
        column_sum.append(summa)
    matrix.append(column_sum)

    # output matrix with results
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:>7}'.format(matrix[i][j]), end='')
        print()


if __name__ == "__main__":
    get_matrix()
