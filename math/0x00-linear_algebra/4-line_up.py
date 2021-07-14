#!/usr/bin/env python3
''' line up '''


def add_arrays(arr1, arr2):
    ''' returns sum of 2 arrays '''
    if len(arr1) != len(arr2):
        return None
    add_arr = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            add_arr.append(arr1[i] + arr2[j])
    return add_arr
