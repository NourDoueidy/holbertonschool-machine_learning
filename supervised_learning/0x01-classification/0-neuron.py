#!/usr/bin/env python3
''' Neuron '''


import numpy as np


class Neuron:
    ''' Defines a class neuron '''

    def __init__(self, nx):
        ''' Constructor '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.w = np.ndarray((1, nx))
        self.w[0] = np.random.normal(sixe=nx)
        self.b = 0
        self.A = 0
