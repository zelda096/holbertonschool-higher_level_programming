#!/usr/bin/python3
"""
Function: matrix_divided().

"""


def matrix_divided(matrix, div):

    """
    Args:
    matrix: list of lists
    div: number int or float
    Return:
    the div
    """

    tyerr = "div must be a number"
    divceroerr = "division by zero"
    tyerrsize = "Each row of the matrix must have the same size"
    errtype = "matrix must be a matrix (list of lists) of integers/floats"
    empty = []

    if matrix == empty or not isinstance(matrix, list):
        raise TypeError(errtype)

    if not isinstance(div, (int, float)):
        raise TypeError(tyerr)

    if len(matrix[0]) == 0:
        raise TypeError(errtype)

    if not all(isinstance(item, list) for item in matrix):
        raise TypeEror(errtype)

    if div == 0:
        raise ZeroDivisionError(divceroerr)

    matrixformat = []

    for row in matrix:

        count = 0

        if len(row) != len(matrix[0]):
            raise TypeError(tyerrsize)
        for count in row:
            if isinstance(count, (int, float)):
                count = int(count)
            else:
                raise TypeError(errtype)

    matrixformat = [[round(count / div, 2) for count in row] for row in matrix]
    return(matrixformat)
