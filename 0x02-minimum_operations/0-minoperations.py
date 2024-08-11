#!/usr/bin/python3
"""Performs minimum Operations """


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    current = 2
    while current <= n:
            if n % current == 0:
                operations += current
                n = n / current
                current -= 1
            current += 1

    return operations

            # reduce root to find remaining smaller vals that evenly-divide n
            #root -= 1
