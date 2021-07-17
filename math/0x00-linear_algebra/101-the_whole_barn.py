#!/usr/bin/env python3
''' the whole barn '''


shape = __import__("2-size_me_please").matrix_shape
add_arrays = __import__("4-line_up").add_arrays
add_matrices2D = __import__("5-across_the_planes").add_matrices2D


def add_matrices(mat1, mat2):
    ''' return sum of two matrices '''
    if shape(mat1) != shape(mat2):
        return None

    if type(mat1[0]) is int:
        return add_arrays(mat1, mat2)
    result = []
    if type(mat1[0][0]) is int:
        return add_matrices2D(mat1, mat2)
    for i in range(len(mat1)):
        result.append(add_matrices(mat1[i], mat2[i]))
    return result
