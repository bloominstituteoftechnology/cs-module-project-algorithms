#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  return combinations(n, [])
  
def combinations(n, current_list):
  choices = ["rock", "paper", "scissors"]
  
  if len(current_list) == 0:
    if n < 1:
      return [[]]
    return combinations(n - 1, [[c] for c in choices])
  
  if n < 1:
    return current_list
  
  new_list = []
  for combo in current_list:
    for choice in choices:
      new_combo = combo.copy()
      new_combo.append(choice)
      new_list.append(new_combo)
      
  return combinations(n - 1, new_list)




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')