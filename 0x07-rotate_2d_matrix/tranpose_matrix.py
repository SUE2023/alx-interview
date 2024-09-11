#!/usr/bin/python3
""" Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """ Roate 2D Matrix 90 degree closewise"""
    N = len(matrix)
    # Consider all squares one by one
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = matrix[y][x]

            # move values from left to bottom
            matrix[y][x] = matrix[x][N-1-y]

            # move values from top to left
            matrix[x][N-1-y] = matrix[N-1-y][N-1-x]

            # move values from right to top
            matrix[N-1-y][N-1-x] = matrix[N-1-x][y]

            # assign temp to right
            matrix[N-1-x][y] = temp
