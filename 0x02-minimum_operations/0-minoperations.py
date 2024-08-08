#!/usr/bin/python3
"""Performs minimum Operations """


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0

    operations = 0
    current = 1
    while current < n:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                operations += i
                current *= i
                break
            else:
                operations += (n - current)
                current = n

    return operations
