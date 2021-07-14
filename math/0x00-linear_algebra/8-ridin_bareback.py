#!/usr/bin/env python3
''' riding breback '''


def mat_mul(mat1, mat2):
    ''' multiply 2 matrices '''
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for i in range(len(mat1)): 
        for j in range(len(mat2)):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[j][k]
    return result
