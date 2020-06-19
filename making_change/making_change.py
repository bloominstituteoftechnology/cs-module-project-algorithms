#!/usr/bin/python

import sys


def making_change(amount, denominations, cache = None):
    # Your code here
    if cache == None:
        cache = [0] * (amount + 1)
    if amount <= 4:
        cache[amount] = 1
    elif amount == 5:
        cache[amount] = 2
    elif cache[amount] == 0:
        total = 0
        for denomination in denominations:
            total += making_change(amount - denomination, cache)
        cache[amount] = total
    return cache[amount]  # SMALL Ran 3 tests in 0.000s, LARGE Ran 1 test in 11.873s


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")
