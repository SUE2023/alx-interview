#!/usr/bin/python3
"""
Print's Pascal Triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    ptriangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(ptriangle[i-1][j-1] + ptriangle[i-1][j])
        row.append(1)
        ptriangle.append(row)
    
    return ptriangle

