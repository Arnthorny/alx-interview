#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write a
method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    Minimum Operations function
    """
    init_n = n
    total = 0
    divisor = 2
    while n > 1:
        if divisor >= init_n:
            return 0
        if n % divisor == 0:
            n = int(n / divisor)
            total += divisor
        else:
            divisor = 3 if divisor == 2 else divisor + 2

    return total
