"""
This module provides a function to calculate the absolute value of a number.
"""


def absolute(x):
    """
    Calculate the absolute value of a number.

    Parameters:
    x (int or float): The number to find the absolute value of.

    Returns:
    int or float: The absolute value of the input number.
    """
    z = 0

    if x >= 0:
        z = x
    else:
        z = (-1) * x

    return z
