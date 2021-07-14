#!/usr/bin/env python3
''' across the planes '''


def add_matices2D(mat1, mat2):
    ''' returns the sum of 2 matrices '''
    if len(mat1) != len(mat2): 
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    sum_mat = []
    for i in range(len(mat1)):
        for j in range(len(mat1[0]):
            sum_mat.append([mat1[i][j] + mat2[i][j])
    return sum_mat
