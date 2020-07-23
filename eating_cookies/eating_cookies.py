"""
Input: an integer
Returns: an integer
"""
from itertools import combinations_with_replacement, permutations
from time import time


def eating_cookies(n):
    if n == 0:
        return 1

    array = [x for x in range(1, n + 1)]
    out = []

    for x in array:
        out.extend([permutations(y)
                    for y in combinations_with_replacement(range(1, 4), x)
                    if sum(y) == n
                    if y not in out])

    out = [x for y in out for x in y]

    return len(dict.fromkeys(out))


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    start = time()
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
    print(time() - start)
