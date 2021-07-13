#!/usr/bin/env python3
''' shape of a matrix '''

def matrix_shape(matrix):
    ''' calculates shape of the matrix '''
    shape = []
    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
