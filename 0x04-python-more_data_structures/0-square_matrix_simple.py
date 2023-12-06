#!/usr/bin/python3
new_matrix = []


def square_matrix_simple(matrix=[]):
    for i in matrix:
        row_matrix = []
        for j in i:
            result = j * j
            row_matrix.append(result)
        new_matrix.append(row_matrix)
    return new_matrix
