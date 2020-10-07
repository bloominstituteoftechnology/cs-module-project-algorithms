#!/usr/bin/python
"""
The Knapsack Problem
​
We have a bunch of objects, we want to maximize the value of our haul.
​
The knapsack has limited weight capacity.
​
Items have weights and values.
​
Which items do we take to maximize value?

"""

"""
Different general approaches
​
* Naive--whatever you came up with first, no matter how inefficient
* Brute Force--Try everything and choose the best one
* Greedy--make the move that's most to your current advantage
"""

'''Explorer's Dilemna - aka the Knapsack Problem
After spending several days exploring a deserted island out in the Pacific, 
you stumble upon a cave full of pirate loot! There are coins, jewels, 
paintings, and many other types of valuable objects.
​
However, as you begin to explore the cave and take stock of what you've 
found, you hear something. Turning to look, the cave has started to flood! 
You'll need to get to higher ground ASAP. 
​
There IS enough time for you to fill your backpack with some of the items 
in the cave. Given that...
- you have 60 seconds until the cave is underwater
- your backpack can hold up to 50 pounds
- you want to maximize the value of the items you retrieve (since you can 
only make one trip)
​
HOW DO YOU DECIDE WHICH ITEMS TO TAKE?
'''
import random
import time
from itertools import combinations 

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f'{self.name}, {self.weight} lbs, ${self.value}'

small_cave = []
medium_cave = []
large_cave = []


def fill_cave_with_items():
    '''Randomly generates Item objects and 
    creates caves of different sizes for testing
    '''
    names = ["painting", "jewel", "coin", "statue", "treasure chest", 
              "gold", "silver", "sword", "goblet", "hat"]

    for _ in range(5):
        n = names[random.randint(0,4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))

    for _ in range(15):
        n = names[random.randint(0,4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        medium_cave.append(Item(n, w, v))

    for _ in range(25):
        n = names[random.randint(0,4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        large_cave.append(Item(n, w, v))


def print_results(items, knapsack):
    '''Print out contents of what the algorithm  
    calculated should be added to the knapsack
    '''
    # print(f'\nItems in the cave:')
    # for i in items:
    #     print(i)

    total = 0

    print('\nBest items to put in knapsack:\n')
    for item in knapsack:
        #print(f'* {item}')
        total += item.value

    print(f'\nTotal value: ${total}')
    print(f'\nResult calculated in {time.time()-start:.5f} seconds')

    print('\n-------------------------')


def naive_fill_knapsack(sack, items):
    '''# Put highest value items in knapsack until full
    (other basic, naive approaches exist)
    '''
    #items.sort(key=lambda item: item.value, reverse=True)

    sack.clear()  # Dump everything out

    # put items in knapsack until full
    weight = 0

    for i in items:
        weight_remaining = 50 - weight

        if i.weight <= weight_remaining:
            sack.append(i)
            weight += i.weight

    return sack


def brute_force_fill_knapsack(sack, items):
    ''' Try every combination to find the best'''

    sack.clear()

    # generate all possible combinations of items
    combos = []

    for i in range(1, len(items) + 1):
        list_of_combos = list(combinations(items, i))

        for combo in list_of_combos:
            combos.append(list(combo))

    # calculate the value of all combinations
    best_value = -1

    for c in combos:
        value = 0
        weight = 0

        for item in c:
            value += item.value
            weight += item.weight

        # find the combo with the highest value
        if weight <= 50 and value > best_value:
            best_value = value
            sack = c

    return sack


def greedy_fill_knapsack(sack, items):
    '''Use ratio of [value] / [weight] 
    to choose items for knapsack
    '''

    # calculate efficiencies
    for i in items:   # O(n) over the number items
        i.efficiency = i.value / i.weight

    # sort items by efficiency
    """
    def sort_func(item):
        return item.efficiency
​
    items.sort(key=sort_func, reverse=True)
    """
    items.sort(key=lambda item: item.efficiency, reverse=True)

    sack.clear()  # Dump everything out

    # put items in knapsack until full
    weight = 0

    for i in items:  # O(n) over the number of items
        weight_remaining = 50 - weight

        if i.weight <= weight_remaining:
            sack.append(i)
            weight += i.weight

    return sack


# TESTS -
# Below are a series of tests that can be utilized to demonstrate
# the differences between each approach. Timing is included to give
# students an idea of how poorly some approaches scale. However, 
# efficiency should also be formalized using Big O notation.

fill_cave_with_items()
knapsack = []

# Test 1 - Naive
print('\nStarting test 1, naive approach...')
#items = medium_cave
items = large_cave
start = time.time()
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# # Test 2 - Brute Force
print('Starting test 2, brute force...')
#items = medium_cave
items = large_cave
start = time.time()
knapsack = brute_force_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# Test 3 - Brute Force
# print('Starting test 3, brute force...')
# items = large_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)

 # Test 4 - Greedy
print('Starting test 4, greedy approach...')
#items = medium_cave
items = large_cave
start = time.time()
greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# Test 5 - Greedy
#print('Starting test 5, greedy approach...')
#items = large_cave
#start = time.time()
#greedy_fill_knapsack(knapsack, items)
#print_results(items, knapsack)

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here

    pass


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