#!/usr/bin/env python3
''' riding breback '''


def mat_mul(mat1, mat2):
    ''' multiply 2 matrices '''
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for r in range(len(mat1)):
        row = []
        for c in range(len(mat2[0])):
            i = 0
            for j in range(len(mat1[0])):
                k = mat1[r][j] * mat2[j][c]
                i += k
            row.append(i)
        result.append(row)
    return result
