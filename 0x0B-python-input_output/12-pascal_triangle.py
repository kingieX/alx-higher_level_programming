#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """returns a list of integers representing the pascal's triangle of n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        angle = triangles[-1]
        tmp = [1]
        for i in range(len(angle) - 1):
            tmp.append(angle[1] + angle[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
