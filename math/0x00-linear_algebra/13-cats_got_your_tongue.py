#!/usr/bin/env python3
''' Concatinating '''
import numpy as np


def np_cat(mat1, mat2, axis=0):
    ''' concatenate 2 matrices along a specific axis '''
    return np.append(mat1, mat2, axis=axis)
