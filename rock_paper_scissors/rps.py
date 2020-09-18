#!/usr/bin/python

import sys

def rock_paper_scissors(n, lst = ('rock', 'paper', 'scissors')):
  if n == 0:
    return [[]]

  out = []
  for i in range(0, len(lst)):
    m = lst[i]
    rem = lst[i+1:]

    for p in rock_paper_scissors(n-1, rem):
      out.append([m]+p)
  return out

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')