#!/usr/bin/python3
"""N queens problem solver"""

import sys


def queens(N, r=0, a=[], b=[], c=[]):
    """Generates all possible solutions for the N queens problem."""
    if r == N:
        yield a
    else:
        for i in range(N):
            if i not in a and i + r not in b and i - r not in c:
                yield from queens(N, r + 1, a + [i], b + [i + r], c + [i - r])


def solve(N):
    """Solve the N queens problem and print all solutions."""
    for solution in queens(N):
        print([[i, solution[i]] for i in range(N)])


def nqueens(argv):
    """Main entry point for the N queens problem solver."""
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solve(N)


if __name__ == "__main__":
    nqueens(sys.argv)
