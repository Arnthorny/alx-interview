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

    coins.sort(reverse=True)

    # This array stores the solutions for each sub-problem
    total_1 = total + 1
    dp_cache = [total_1]  * (total_1)
    dp_cache[0] = 0

    # Loop through every sub-problem in dp_arr. From index = 0 to index = total
    for i in range(1, total_1):
        for coin in coins:
            # Check that current coin value is less than current sub-problem.
            if coin <= i:
                # If previous sub-problem solution exists in cache
                tmp = dp_cache[i - coin] + 1
                # Compare with the current minimum
                dp_cache[i] = total_1 if total_1 < tmp else tmp
                break

        # Set the soln of curent sub-problem to be the minimum

    # If value at index of sub-problem exceeds the sub-problem, then no valid
    # solution. Else the value at that index is the solution.
    return -1 if dp_cache[total] > total else dp_cache[total]
