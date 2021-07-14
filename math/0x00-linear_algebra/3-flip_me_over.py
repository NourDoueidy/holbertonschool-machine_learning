#!/usr/bin/env python3
''' flip me over '''


def matrix_transpose(matrix):
    ''' transpose without numpy '''
    matrix_transpose = 0
    for i in len(matrix):
        for j in len(matrix[0]):
            matrix_transpose[j][i] = matrix[i][j]
    return matrix_transpose
