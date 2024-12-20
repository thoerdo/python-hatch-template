"""
This module provides a function to divide one number by another.
"""


def divide(a, b):
    """
    Divide one number by another.

    Parameters:
    a (int or float): The dividend.
    b (int or float): The divisor.

    Returns:
    float: The result of the division.

    Raises:
    ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
