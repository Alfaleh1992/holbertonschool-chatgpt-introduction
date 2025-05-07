#!/usr/bin/python3
import sys


def factorial(n):
    """
    Description:
        Recursively computes the factorial of a
        non‑negative integer n (n!).

    Parameters:
        n (int): The non‑negative integer whose factorial
                 is to be calculated.

    Returns:
        int: 1 if n is 0 (base case);
             otherwise n multiplied by factorial(n - 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
