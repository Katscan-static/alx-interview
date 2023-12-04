#!/usr/bin/python3
""" This module returns a list of lists that has pascals triangle. """


def pascals_triangle(n):
    """Generate Pascal's triangle with 'n' rows.

    This function creates Pascal's triangle up to 'n'.

    Args:
    - n (int): The number of rows to generate for Pascal's triangle.

    Returns:
    - list: A list of lists representing Pascal's triangle.
    """

    temp = []
    pascals_init = [1]

    if n <= 0:
        return temp

    for i in range(n):
        row = [1] * (i + 1)
        temp.append(row)

        if i > 1:
            for c in range(1, i):
                try:
                    temp[i][c] = temp[i - 1][c - 1] + temp[i - 1][c]
                except IndexError:
                    temp[i].append(1)
    return temp
