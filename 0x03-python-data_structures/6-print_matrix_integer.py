#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for num in r:
            print("{:d}".format(num), end=" ")
        print()
