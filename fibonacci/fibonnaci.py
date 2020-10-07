import unittest
import random


cache = {0: 1, 1: 1}

def recursive_fib(n):
    if n in cache:
        return cache[n]

    cache[n] = recursive_fib(n-1) + recursive_fib(n-2)

    return cache[n]

print(recursive_fib(100))