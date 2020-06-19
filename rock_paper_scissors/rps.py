#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  RPSarray = ['rock', 'paper', 'scissors']
  final_array = [[0 for wide in range(n)] for deep in range(3**n)]

  #while counter < n:
  for deep in range(3**n):
    counter = n
    for wide in range(n):
      if wide == n-counter:
        final_array[deep][wide] = RPSarray[(deep//(3**(counter-1))%3)]
        counter -= 1
  return final_array

rock_paper_scissors(4)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]') 