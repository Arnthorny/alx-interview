#!/usr/bin/python3
"""
Module for makeChange
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount `total`,
    given a pile of `coins`
    """
    if total <= 0:
        return 0

    # This array stores the solutions for each sub-problem
    dp_arr = [total + 100] * (total + 1)
    dp_arr[0] = 0

    # Loop through every sub-problem in dp_arr. From index = 0 to index = total
    for i in range(len(dp_arr)):
        for j in range(len(coins)):
            # Check that current coin value is less than current sub-problem.
            if coins[j] <= i:
                # Set the soln of curent sub-problem to be the minimum of
                # its current soln and 1 + the solution to a previously
                # solved sub-problem
                dp_arr[i] = min(dp_arr[i], 1 + dp_arr[i - coins[j]])

    # If value at index of sub-problem exceeds the sub-problem, then no valid
    # solution. Else the value at that index is the solution.
    return -1 if dp_arr[total] > total else dp_arr[total]
