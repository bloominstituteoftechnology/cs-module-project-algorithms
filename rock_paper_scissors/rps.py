#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Create empty list for all possible plays
  possible_plays = []

  # create list of different choices player can make
  choices = ['rock', 'paper', 'scissors']

  #create helper function
  def helper(n, currChoices):
    #create base case - base case will be when n == 0 for each instance of helper
    if n == 0:
      #before returning, append the new choice cobination to the possible plays list 
      possible_plays.append(currChoices)
      return
    # implement recursion. We'll create a loop that inititializes instances of the helper function
    # Within each loop, we'll initialize an instance of the helper function n times, decrementing n on each loop. 
    # Note that each instance of Helper will start another loop / round of helper functions until each is resolved by reaching n == 0
    # Each time a new helper is initialized, it is initialized with a new / additional choice added through the currChoice param
    

    for choice in range(len(choices)):
      list_choice = [choices[choice]]
      helper(n - 1, currChoices + list_choice)
  helper(n, [])
  return possible_plays




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')