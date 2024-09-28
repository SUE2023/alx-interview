#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0  # Perimeter p to keep track of the perimenter
    for i in range(len(grid)):  # i for row
        for j in range(len(grid[i])):  # j for column
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    p += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    p += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    p += 1
    return p
