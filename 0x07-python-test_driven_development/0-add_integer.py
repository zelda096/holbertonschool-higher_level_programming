#!/usr/bin/python3
"""
 Function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Args:
    a: int or float
    b: int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a_int = int(a)
    b_int = int(b)
    sum = a_int + b_int
    return (sum)
