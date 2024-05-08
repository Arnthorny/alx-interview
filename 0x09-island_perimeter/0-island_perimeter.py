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

            perimeter += 4
            top = 0 if (row - 1 < 0) else\
                (-1 if (grid[row - 1][col] == 1) else 0)

            perimeter += top

            down = 0 if (row + 1 >= no_rows) else \
                (-1 if (grid[row + 1][col] == 1) else 0)

            perimeter += down

            left = 0 if (col - 1 < 0) else \
                (-1 if (grid[row][col - 1] == 1) else 0)

            perimeter += left

            right = 0 if (col + 1 >= no_cols) else \
                (-1 if (grid[row][col + 1] == 1) else 0)

            perimeter += right

    return perimeter
