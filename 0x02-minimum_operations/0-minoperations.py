#!/usr/bin/python3
"""
    this module check the minimum number of operations it would take to get n
"""


def minOperations(n):
    """
        minOperations:
        this is the function for minimum operations

        Args:
            n (int): the number to get the minimum operations to

        Returns:
            int - number of operations
    """
    if n <= 1:
        return 0

    min_ops = n

    for i in range(2, n):
        if n % i == 0:
            ops = minOperations(n // i) + i
            if ops < min_ops:
                min_ops = ops

    return min_ops
