#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    output = []
    plays = ['rock', 'paper', 'scissors']

    def build_moves(moves_remaining, moves=[]):
        if moves_remaining == 0:
            output.append(moves)
        else:
            for play in plays:
                build_moves(moves_remaining - 1, [*moves, play])
        return output

    return build_moves(n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')