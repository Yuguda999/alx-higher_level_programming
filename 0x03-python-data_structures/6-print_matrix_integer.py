#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        fmt = " ".join(["{:d}" for x in row])
        print(fmt.format(*row))
