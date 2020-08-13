#!/usr/bin/python

import sys
# def num_coins(cents):
#   coins = [25,10,5,1]
#   count = 0
#   for c in coins:
#     while cents>= c:
#       cents = cents -c 
#       count = count + 1
      
#   return count


 
    
def making_change(amount, denominations):
  # Your code here
  count = 0
  coins = [1,5,10,25,50]
  ways = 0
  for c in coins:
    while amount <=c:
      count =count +1
      amount = amount -1
      ways = ways +1
    
   


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")