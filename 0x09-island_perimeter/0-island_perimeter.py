#!/usr/bin/python3
"""
Module for island perimeter
"""


def island_perimeter(grid):
    """
    Function to calculate perimeter of island
    """

    no_cols = len(grid[0])
    no_rows = len(grid)
    perimeter = 0

    for row in range(no_rows):
        for col in range(no_cols):
            if grid[row][col] != 1:
                continue

            top = None if (row - 1 < 0) else\
                (None if (grid[row - 1][col] == 1) else (row - 1, col))

            if top is not None:
                perimeter += 1

            down = None if (row + 1 >= no_rows) else \
                (None if (grid[row + 1][col] == 1) else (row + 1, col))

            if down is not None:
                perimeter += 1

            left = None if (col - 1 < 0) else \
                (None if (grid[row][col - 1] == 1) else (row, col - 1))

            if left is not None:
                perimeter += 1

            right = None if (col + 1 >= no_cols) else \
                (None if (grid[row][col + 1] == 1) else (row, col + 1))

            if right is not None:
                perimeter += 1

    return perimeter
