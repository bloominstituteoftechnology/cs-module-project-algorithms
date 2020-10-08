#!/usr/bin/python

import sys
import random

def rock_paper_scissors(n):
  # Your code here
  rps = ["Rock", "Paper", "Scissors"]
  return rps[random.randint(0, 2)]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')