#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  if n == 0:
    return [[]]
  moves = [["rock"], ["paper"], ["scissors"]]
  return helper(n, moves)

def helper(n, moves):
  if len(moves[0]) == n:
    return moves
  result = []
  for move in moves:
    for add_on in ["rock", "paper", "scissors"]:
      curr = move[:]
      curr.append(add_on)
      result.append(curr)
  return helper(n, result)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')