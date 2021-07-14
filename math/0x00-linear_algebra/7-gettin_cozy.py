#!/usr/bin/env python3
''' getting cozy '''


def cat_matrices2D(mat1, mat2, axis=0):
    ''' Concatenate 2 matrices along a specific axis '''
    if len(mat1) != len(mat2) and axis == 1:
        return None
    if len(mat1[0]) != len(mat2[0]) and axis == 0:
        return None
    
    cat_mat = []
    
    if axis == 0:
        cat_mat = mat1 + mat2
    elif axis == 1:
        for r in range(len(mat1)):
            rows = []
            for c in range(len(mat1[0])):
                rows.append(mat1[r][c])
            for c in range(len(mat2[0])):
                rows.append(mat2[r][c])
            cat_mat.append(rows)

    return cat_mat
