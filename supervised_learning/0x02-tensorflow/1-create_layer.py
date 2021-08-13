#!/usr/bin/env python3
''' Create Layer '''


import tensorflow as tf


def create_layer(prev, n, activation):
    ''' create a tensorflow layer '''
    initializer = (tf.contrib.layers.
                   variance_scaling_initializer(mode="FAN_AVG"))
    return tf.layers.Dense(n, activation, name='layer',
                           kernel_initializer=initializer)(prev)
