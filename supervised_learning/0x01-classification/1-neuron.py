#!/usr/bin/env python3
''' Neuron '''


import numpy as np


class Neuron:
    ''' Defines a class Neuron '''

    def __init__(self, nx):
        ''' Constructor '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.ndarray((1, nx))
        self.__W[0] = np.random.normal(size=nx)
        self.__b = 0
        self.__A

    @property
    def W(self):
        ''' Weights '''
        return self.__W

    @property
    def b(self):
        ''' bias '''
        return self.__b

    @property
    def A(self):
        ''' activation values '''
        return self.__A
