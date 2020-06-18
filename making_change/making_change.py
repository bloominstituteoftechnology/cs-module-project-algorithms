#!/usr/bin/python

import sys

# def change(amount, x)
#   amount = amount - x

#   if amount == 0:
#     return 1
#   elif amount < 0:
#     return
#   else:
#     change(amount, x)

# def making_change(amount, denominations):
#   # Your code here
#   print(len(denominations))
#   #base case 
#   for x in range(len(denominations)):
#     amount = amount - denominations[x]
#     if amount == 0:
#       return 1
#     elif amount < 0:
#       return 
#     else:
#       making_change(amount, denominations)

# print(making_change(10, [1, 5, 10]))

# def making_change(amount, denominations):
  # Your code here

  #base case 
  

  # if amount == 0:
  #   return 1
  # elif amount < 0:
  #   return 0
  # elif len(denominations) <= 0 and amount > 0:
  #   return 0
  # else:
  #   return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[0:-1])

def making_change(amount, denominations):
  ways = [0] * (amount + 1)
  ways[0] = 1
  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      remainder = higher_amount - coin
      ways[higher_amount] += ways[remainder]
  return ways[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")