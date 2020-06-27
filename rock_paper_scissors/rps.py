#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #game will be final result array
  game = []
  #all options
  plays = [['rock'], ['paper'], ['scissors']]
  if n == 0:
    return game
  # num
  if n == 1:
    return plays
  #recursive runs and returns plays until 0
  for newList in rock_paper_scissors(n-1):
    #loop through all options and add it to the existing list
    for play in plays:
      print('newList', newList)
      game.append(newList + play)
      
  return game

  
rock_paper_scissors(2)





  # Your code here
  # options = ['rock', 'paper', 'scissors']
  # #num of possible options
  # elements = len(options) ** n
  # # will make a list of 0 for each possible combo
  # num_of_options = [0] * elements
  # #dictonary
  # dictonary = {i : 0 for i in range (elements)}
  # print(dictonary)

  # print(num_of_options)

 
  
  #options_per = num_of_options / 3

  # for x in options_per:
  #   num_of_options[x] = [options[x], 'rock']

  # for x in options_per:
 

rock_paper_scissors(2)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')