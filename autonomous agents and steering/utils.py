"""
Module containing utility functions
"""


def remap(x, in_min, in_max, out_min, out_max):
    """
    Map input value (knowing minimum and maximum values that it can take) to another range

    :param x: value to be mapped
    :param in_min: minimum value of input
    :param in_max: maximum value of input
    :param out_min: minimum value of output
    :param out_max: maximum value of output
    :return: changed value
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
