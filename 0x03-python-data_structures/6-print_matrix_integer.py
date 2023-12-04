#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print(f"{row[i]}".format(), end=" " if i != len(row) - 1 else "")
        print()
