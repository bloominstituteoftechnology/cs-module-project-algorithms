'''
The idea is that we have a backpack with
a size or weight limit that constrains
how many things we can put inside.
​
We have lots of items we want to put into
the knapsack. However, they won't all fit.
Choosing the optimal combination of items
that meets size or weight constraints while
maximizing value might seem doable with a
small example, but this becomes a difficult
problem very quickly.
'''

from itertools import combinations


def naive_fill_knapsack(sack, items):
    '''# Put highest value items in knapsack until full
    (other basic, naive approaches exist)
    '''
    # sort items by value
    items.sort(key=lambda x: x.value, reverse=True)

    sack = []
    weight = 0
    # put most valuable items in knapsack until full
    for i in items:
        weight += i.weight
        if weight > 50:
            return sack
        else:
            sack.append(i)

    return sack


def brute_force_fill_knapsack(sack, items):
    ''' Try every combination to find the best'''

    # generate all possible combinations of items
    combos = []
    sack = []
    for i in range(1, len(items)+1):
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            combos.append(list(combo))

    best_value = -1
    # calculate the value of all combinations
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
    for i in items:
        i.efficiency = i.value/i.weight

    # sort items by efficiency
    items.sort(key=lambda x: x.efficiency, reverse=True)

    # put items in knapsack until full
    sack = []
    weight = 0
    for i in items:
        weight += i.weight
        if weight > 50:
            return sack
        else:
            sack.append(i)

    return sack
