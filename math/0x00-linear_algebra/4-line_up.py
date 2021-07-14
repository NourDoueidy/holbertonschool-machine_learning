#!/usr/bin/env python3
''' line up '''


def add_arrays(arr1, arr2):
    ''' returns sum of 2 arrays '''
    add_arr = []
    for i in len(arr1):
         for j in len(arr2):
             add_arr.append(i + j)
    return add_arr
