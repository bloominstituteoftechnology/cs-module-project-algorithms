"""
Input: an integer
Returns: an integer
"""


def memoize(f):
    cache = {}

    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper


@memoize
def eating_cookies(n):
    if n > 0:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
    elif n == 0:
        return 1
    else:
        return 0





if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
