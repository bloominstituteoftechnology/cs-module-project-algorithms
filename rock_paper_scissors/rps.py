#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # BASE CASE: if n is 0
  if n is 0:
    return [[]]

  # Set up rock, paper, scissors list to draw permutations from
  options = ['rock', 'paper', 'scissors']

  # Set up a result list to store all possible combinations
  result = []

  # Define an inner method to use for recursion
  def rounds(round, roundNum):
    # Loop for elements in the options list
    for i in options:
      # Add each element to the round list
      round.append(i)

      # Once roundNum is the same as n, append round list to result
      if roundNum == n:
        result.append(round)
      # Otherwise, recursively call round method and add one to roundNum
      else:
        rounds(round, roundNum + 1)

      # Remove last element from round list before iterating back through for loop
      round.pop()
  
  rounds([], 1)
  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')