"""
Algorithms, stretch problem 2
"""

import sys

def making_change(amount, coins, cache=None):
    """
    Receives as input an amount of money in cents as well as an array of coin
    denominations and calculates the total number of ways in which change can
    be made for the input amount using the given coin denominations.
    """
    if amount == 0:
        return 1

    if len(coins) == 1:
        if amount % coins[0] == 0:
            return 1
        return 0
    
    else:
        if cache is None:
            cache = {}

        if (amount, len(coins)) in cache:
            return cache[(amount, len(coins))]

        combinations = 0
        for i in range(amount // coins[-1] + 1):
            new_amount = amount - coins[-1] * i
            if (new_amount, len(coins) - 1) not in cache:
                cache[(new_amount, len(coins) - 1)] = making_change(new_amount,
                                                                   coins[:-1],
                                                                   cache)
            combinations += cache[(amount - coins[-1] * i, len(coins) - 1)]
        return combinations

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denom = [1, 5, 10, 25, 50]
        amt = int(sys.argv[1])
        print("There are {ways} ways to make {amt} "
              "cents.".format(ways=making_change(amt, denom), amt=amt))
    else:
        print("Usage: making_change.py [amount]")
