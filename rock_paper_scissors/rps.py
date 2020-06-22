#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  options = ['rock', 'paper', 'scissors']
  #num of possible options
  elements = len(options) ** n
  # will make a list of 0 for each possible combo
  num_of_options = [0] * elements
  #dictonary
  dictonary = {i : 0 for i in range (elements)}
  print(dictonary)

  print(num_of_options)


  
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