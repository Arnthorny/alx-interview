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
    visited = set()

    for row in range(no_rows):
        for col in range(no_cols):
            if grid[row][col] != 1:
                continue

            top = None if (row - 1 < 0) else\
                (None if (grid[row - 1][col] == 1) else (row - 1, col))

            if top is not None and top not in visited:
                perimeter += 1
                visited.add(top)

            down = None if (row + 1 >= no_rows) else \
                (None if (grid[row + 1][col] == 1) else (row + 1, col))

            if down is not None and down not in visited:
                perimeter += 1
                visited.add(down)

            left = None if (col - 1 < 0) else \
                (None if (grid[row][col - 1] == 1) else (row, col - 1))

            if left is not None and left not in visited:
                perimeter += 1
                visited.add(left)

            right = None if (col + 1 >= no_cols) else \
                (None if (grid[row][col + 1] == 1) else (row, col + 1))

            if right is not None and right not in visited:
                perimeter += 1
                visited.add(right)

    return perimeter
