#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    long = len(matrix)

    for i in range(long):
        for j in range(len(matrix[i])):
            print('{:d}'.format(matrix[i][j]), end="")
            if j < len(matrix[i])-1:
                print('', end=" ")
        print()
