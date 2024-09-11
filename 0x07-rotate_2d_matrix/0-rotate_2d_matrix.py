#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix 90 degrees clockwise """
    N = len(matrix)
    for i in range(int(N / 2)):
        y = (N - i - 1)
        for j in range(i, y):
            x = (N - 1 - j)
            # current number
            tmp = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[x][i]
            # change left for bottom
            matrix[x][i] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = tmp
