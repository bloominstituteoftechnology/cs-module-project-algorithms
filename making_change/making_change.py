#!/usr/bin/python

import sys



# def making_change(amount, denominations):
  
#   cache = [0 for amount in range(amount+1)]
#   cache[0] = 1

#   if amount <= 1:
#     return cache[0]

#   for coin in denominations:
#     for i in range(amount+1):
#       if i >= coin:
#         cache[i] += cache[i - coin]

#   return cache[amount]

def making_change(amount, denominations, cache=None):
  if cache is None:
      cache = {}

  if amount == 0 and amount < 5:
    return 1

  if amount < 0:
    return 0
  
  if cache and cache[amount]:
    return cache[amount]


  for coin in denominations:
    cache[amount] = making_change(amount-coin, denominations)
 
  return cache[amount]




if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")