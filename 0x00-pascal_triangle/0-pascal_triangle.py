#!/usr/bin/python3
"""
Print's Pascal Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.
    Returns:
    List[List[int]]: A list of lists representing Pascal's Triangle.
    If n <= 0, an empty list is returned.
    """
    if n <= 0:
        return []

    ptriangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):   # Generates each row of Pascal's Triangle
        row = [1]  # The first element of each row is always 1
        for j in range(1, i):  # Calculate the intermediate values of the row
            row.append(ptriangle[i-1][j-1] + ptriangle[i-1][j])
        row.append(1)  # The last element of each row is always 1
        ptriangle.append(row)

    return ptriangle

