#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
def sort(items):
      for i in range(0,len(items)-1):
            current = i
            smallest = i
            for j in range(current + 1, len(items)):
                  if (items[j].value / items[j].size) > (items[i].value / items[i].size):
                        smallest = j
            items[current],items[smallest] = items[smallest],items[current]
      return items
    
def knapsack_solver(items, capacity):
      sort = sort(items)
      sum = 0
      while sum < capacity:
        for k in range(0,len(sort)):
            sum += sort[k].size
        return k
      return sort[:k+1]

    


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')