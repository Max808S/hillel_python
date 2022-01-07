import random


def get_matrix():
    """
    Generates a lists with random numbers of the size entered by the user.
    Calculates the sum of each row and column. Print lists as a matrix.
    """
    m = int(input('Enter the number of strings: '))
    n = int(input('Enter the number of columns: '))
    matrix = [[random.randint(1, 50) for i in range(n)] for j in range(m)]
    column_sum = []

    print(f'Strings: {n}. Columns: {m}.\n')

    # calculated the sum of the elements of the strings of the matrix
    for i in range(m):
        summa = 0
        for j in range(n):
            summa += matrix[i][j]
        matrix[i].append(summa)

    # calculated the sum of the elements of the columns of the matrix
    for i in range(n):
        summa = 0
        for j in range(m):
            summa += matrix[j][i]
        column_sum.append(summa)
    matrix.append(column_sum)

    # output of a matrix with the sums of strings and columns
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:>7}'.format(matrix[i][j]), end='')
        print()


if __name__ == "__main__":
    get_matrix()
