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
    hold1 = n
    if n > 1:
        for i in range(2, n):
            if not (n % i) and (n/i + i) < hold1:
                hold1 = (n/i + i)
            elif (n/i + i) > hold1:
                return int(hold1)
    return 0
