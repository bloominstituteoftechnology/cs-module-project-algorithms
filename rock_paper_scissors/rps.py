#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possible_moves = ['rock', 'paper', 'scissors']
  basic = [['rock'], ['paper'], ['scissors']]

  if n == 0:
    return [[]]
  if n == 1:
    return basic
  if n > 1:
    diff = n - 1
    passed_list = basic
  for _ in range(diff):
    new_list = []
    for item in passed_list:
      for move in possible_moves:
        new_list.append(item + [move])
    passed_list = new_list
  return new_list

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
