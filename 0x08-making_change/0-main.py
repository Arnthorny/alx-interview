#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
print(makeChange([1, 3, 5, 6, 9], 90))
print(makeChange([1, 2, 3], 10))
print(makeChange([2], 5))
print(makeChange([1], 9))
