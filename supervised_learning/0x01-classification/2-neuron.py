#!/usr/bin/env python3
''' Neuron forward propagation '''

import numpy as np


class Neuron:
    ''' Defines class Neuron '''

    def __init__(self, nx):
        ''' nx: number of input features '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.ndarray((1, nx))
        self.__W[0] = np.random.normal(size=nx)
        self.__b = 0
        self.__A = 0
