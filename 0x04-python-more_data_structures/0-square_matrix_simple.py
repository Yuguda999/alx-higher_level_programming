#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_list = []
    for i in matrix:
        squared_list.append(list(map(lambda x: x ** 2, i)))
    return squared_list
