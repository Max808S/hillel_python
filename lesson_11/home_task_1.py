import random


def create_matrix(m):
    """
    Create matrix with size entered by user and sort by task condition.
    """
    matrix = [[random.randint(1, 50) for i in range(m)] for j in range(m)]
    show_matrix(matrix, f'Generated matrix with size {m}x{m}:')

    # count and add to the matrix the sum of the columns
    column_sum = []
    matrix.append(column_sum)
    for i in range(m):
        summa = 0
        for j in range(m):
            summa += matrix[j][i]
        matrix[-1].append(summa)
    # show_matrix(matrix, 'Matrix with sum row added: ')

    # sorting columns by the sum of their elements
    for i in range(len(matrix)):
        for j in range(1, m):
            if matrix[-1][j - 1] > matrix[-1][j]:
                for k in range(len(matrix)):
                    matrix[k][j], matrix[k][j - 1] = matrix[k][j - 1], matrix[k][j]
    # show_matrix(matrix, 'Matrix after columns sorted by their sum: ')

    # sort odd columns in ascending order, even columns in descending order
    for run in range(m - 1):
        for i in range(m):
            for j in range(m - 1):
                if i % 2 != 0:
                    if matrix[j][i] > matrix[j + 1][i]:
                        matrix[j][i], matrix[j + 1][i] = matrix[j + 1][i], matrix[j][i]
                else:
                    if matrix[j][i] < matrix[j + 1][i]:
                        matrix[j][i], matrix[j + 1][i] = matrix[j + 1][i], matrix[j][i]
    show_matrix(matrix, 'Matrix after sorting: ')


def show_matrix(matrix, text=''):
    """
    Shows matrix output
    """
    print(text)
    for i in range(len(matrix)):
        for j in range(m):
            print("%6d" % matrix[i][j], end='')
        print()


if __name__ == '__main__':
    while True:
        m = int(input('Enter the size of matrix: '))
        if m >= 5:
            create_matrix(m)
            break
        else:
            print('Enter the number bigger 5: ')
