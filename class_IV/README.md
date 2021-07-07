## Runtime complexities:
`O(1)`: constant time
```py
# adding to / removing keys from dictionaries
# 1:1 element comparison
```
`O(n)`: linear time
```py
# Dependent on length/size of array/iterable
# Single loop
```
`O(log n)`: logarithmic time
```py
# Binary search
# Halving as you go
```
`O(n^2)`: quadratic time 
```py
# nested loops
for x in this: # O(n)
    for y in that: # O(n)
        return x, y
```

---

## First Pass --> Optimized Solution Example:
***First Pass:***
```py
def eating_cookies(n):
    # no negative values for n
    if n < 0:
        return 0
    # if "tree" gets down to 0, count that as a way to eat
    if n == 0:
        return 1
    # otherwise, get closer to base case by calling `eating_cookies`
    # on each of the "alternate futures" for how the monster ate
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    # Implementation has O(3^n) runtime complexity due to the fact that there
    # are three possible decisions each time
```
***Optimized Solution:***
```py
def eating_cookies(n, cache):
    # no negative values for n
    if n < 0:
        return 0
    # if "tree" gets down to 0, count that as a way to eat
    if n == 0:
        return 1

    # check the cache to see if it holds the answer this branch is looking for
    elif n in cache:
        return cache[n]

    # otherwise, n is not in cache, so compute answer the "normal" way
    else:
        # once the answer is computed, save it in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

    # This implementation cuts out the redundant work by using a cache, in this
    # case a dictionary, so every n value is only computed once rather than
    # redundantly

    # This reduced runtime from O(3^n) to O(n) but did increase space complexity
```

---