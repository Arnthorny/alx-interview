#!/usr/bin/python3

def sieve(n):
    sieve_list = [True if x > 1 else False for x in range(n + 1)]

    for i in range(int(n ** 0.5)):
        if sieve_list[i] is False:
            continue
        else:
            for j in range(i**2, n + 1, i):
                if j % i == 0:
                    sieve_list[j] = False
    all_primes = [i for i in range(len(sieve_list)) if sieve_list[i]]
    return all_primes


def determine_round_winner(round_n, who_won_arr):
    all_primes_in_range = sieve(round_n)
    all_primes_in_range.reverse()

    who_is_playing = 0  # Maria starts

    while all_primes_in_range:
        all_primes_in_range.pop()
        who_is_playing += 1

    if who_is_playing == 0:  # Maria had nothing to play
        who_won_arr[1] += 1
    else:
        who_won_arr[who_is_playing % 2] += 1


def isWinner(x, nums):
    who_won = [0, 0]

    for rnd in range(x):
        determine_round_winner(nums[rnd], who_won)

    winner = 'Maria' if who_won[0] > who_won[1] else 'Ben'
    return winner if who_won[0] != who_won[1] else None
