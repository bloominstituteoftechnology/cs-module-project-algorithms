#!/usr/bin/python

import sys


def making_change(amount, denominations, memory=None):
  if memory == None:
      memory = [0] * (amount + 1)
  if amount <= 4:
      memory[amount] = 1
  elif amount == 5:
      memory[amount] = 2
  elif memory[amount] == 0:
      total = 0
      for denomination in denominations:
        total += making_change(amount - denomination, memory)
      memory[amount] = total
  return memory[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
