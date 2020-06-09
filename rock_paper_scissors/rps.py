"""
Algorithms, stretch problem 1
"""

import sys

def rock_paper_scissors(n):
    """
    Returns all possible sequences of rock, paper, scissors moves in a game of
    length n.
    """
    if n == 0:
        return [[]]
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]

    plays = rock_paper_scissors(1)
    for _ in range(n - 1):
        new_plays = []
        for move_list in plays:
            for move in rock_paper_scissors(1):
                new_plays += [move_list + move]
        plays = new_plays
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
