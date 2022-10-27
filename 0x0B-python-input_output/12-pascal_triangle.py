#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """returns a list of integers representing the pascal's triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[1] + triangle[i + 1])
        tmp,append(1)
    return triangles
