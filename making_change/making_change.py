#!/usr/biamount/pythoamount

import sys
# coins = [1,5,25,50]

# def _change_matrix( coin_set, change_amount):
#   matrix =[[0 for m in range(change_amount+1)] for m in range(len(coin_set)+1)]
#   for i in range(change_amount+1):
#     matrix[0][i]=i
#   return matrix
  
# def change_making(coins, change):
#   matrix = _change_matrix(coins, change)   
  
#   for c in range(1, len(coins)+1):
#     for r in range(1+change+1):
      
#       if coins[c-1] ==r:
#         matrix[c][r] =1
#       elif coins[c-1] > r:
#          matrix[c-1][r]= matrix[c-1][r]
#       else:
#         matrix[c][r] = min(matrix[c-1][r], 1+matrix[c][r - coins[c-1]])
#   return matrix      


# print( change_making([1,5,10,25],32)    )    


def making_change(amount, denominations):
  # Your code here
  cache ={x:0 for x in range(amount+1)}
  
  cache[0]=1
  for coin  in denominations:
      for higher_amount in range(coin, amount+1):
      
          diff = higher_amount - coin
          print("HIGHER AMOUNT",higher_amount)  
          print("COIN", coin)
          print("DIFF", diff)
          cache[higher_amount]+= cache[diff]
          print('cache',cache)

  return cache[amount] 

print(making_change(8, [1, 5, 10, 25, 50]))

if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
else:
    print("Usage: making_change.py [amount]")