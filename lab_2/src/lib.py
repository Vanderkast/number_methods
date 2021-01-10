import numpy as np


def div_diff(x_list, y_list, n):
    result = 0
    _range = range(n+1)
    for i in _range:
        box = y_list[i]
        for j in _range:
            if(j != i):
                box /= x_list[i]-x_list[j]
        result += box
    return result


def div_diff_matrix(x_list, y_list):
    n = len(x_list)
    matrix = np.zeros((n, n))

    for i in range(n):  # fills first column with y_list values
        matrix[i][0] = y_list[i]

    for j in range(0, n-1):
        for i in range(0, n - j - 1):
            matrix[i][j+1] = (matrix[i][j] - matrix[i+1][j]) \
                / (x_list[i] - x_list[j + 1 + i])

    return matrix


def interpolated_f(x_list, dif_list, x):
    result = 0
    for i in range(len(dif_list)):
        box = dif_list[i]
        for j in range(i):
            box *= (x - x_list[j])
        result += box
    return result
