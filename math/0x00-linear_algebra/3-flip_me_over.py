#!/usr/bin/env python3
''' flip me over '''


def matrix_transpose(matrix):
    ''' transpose without numpy '''
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_transpose = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_transpose.append(row)
    return matrix_transpose
