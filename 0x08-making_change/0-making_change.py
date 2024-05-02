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
    dp_cache = {0: 0}

    # Loop through every sub-problem in dp_arr. From index = 0 to index = total
    for i in range(1, total + 1):
        min_coins = total + 100
        for coin in coins:
            # Check that current coin value is less than current sub-problem.
            if coin <= i:
                # If previous sub-problem solution exists in cache
                if i - coin in dp_cache:
                    # Compare with the current minimum
                    min_coins = min(min_coins, 1 + dp_cache[i - coin])

        # Set the soln of curent sub-problem to be the minimum
        dp_cache[i] = min_coins

    # If value at index of sub-problem exceeds the sub-problem, then no valid
    # solution. Else the value at that index is the solution.
    return -1 if dp_cache[total] > total else dp_cache[total]
