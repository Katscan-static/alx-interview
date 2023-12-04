#!/usr/bin/python3


""" This module returns a list of lists that has pascals triangle. """


def pascal_triangle(n):
    """
    0-pascal_triangle.py:

    Generate Pascal's triangle with 'n' rows.

    This function creates Pascal's triangle up to 'n'.

    Args:
        n (int): The number of rows to generate for Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """

    temp = []

    if n <= 0:
        return temp

    for i in range(n):
        row = [1] * (i + 1)
        temp.append(row)

        if i > 1:
            for c in range(1, i):
                temp[i][c] = temp[i - 1][c - 1] + temp[i - 1][c]
    return temp
