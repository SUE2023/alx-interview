#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matric at 90 degrees clockwise """
    # reversing the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()

    # make transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            # swapping matrix[j][i] and matrix[i][j]
            matrix[i][j], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[j][i], end=' ')
