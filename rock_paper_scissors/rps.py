#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Your code here
    moves = ["rock", "paper", "scissors"]
    moves_ll = [["rock"], ["paper"], ["scissors"]]
    if n == 0:
        return [[]]
    if n == 1:
        return moves_ll
    if n > 1:
        diff = n - 1
        passed = moves_ll
    for i in range(diff):
        list_new = []
        for item in passed:
            for move in moves:
                list_new.append(item + [move])
        passed = list_new
    return list_new


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
