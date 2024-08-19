#!/usr/bin/python3
"""
Module for makeChange
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount `total`,
    given a pile of `coins`
    """
    coins.sort(reverse=True)
    idx, coins_used, no_of_coins = (0, 0, len(coins))

    while total > 0:
        if idx >= no_of_coins:
            return -1
        if total - coins[idx] >= 0:
            coins_used += 1
            total -= coins[idx]
        else:
            idx += 1

    return coins_used
