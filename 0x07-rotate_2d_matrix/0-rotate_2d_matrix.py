#!/usr/bin/python3
"""
Rotate 2d Matrix Function
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate an n x n 2D matrix 90 degrees clockwise
    """

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
