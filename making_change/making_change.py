#!/usr/bin/python

import sys

def making_change(amount, denominations):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    
    num_ways_to_make_change = 0

    for i in range(len(denominations)):
        num_ways_to_make_change += making_change(amount - denominations[i], denominations[i:])

    return num_ways_to_make_change


# denominations = [1, 5, 10, 25, 50]
# print(making_change(500, denominations))

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")