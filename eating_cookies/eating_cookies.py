# For reference:

# def climb_stairs(current, desired):
#     if current > desired:
#         return 0
#     if current == desired:
#         return 1
#     return climb_stairs(current+1, desired) + climb_stairs(current+2, desired)

'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    eaten = 0
    if eaten == n:
        return 1

    if eaten > n:
        return 0

    return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


def eating_cookies_cached(n, cache):
    eaten = 0
    if eaten == n:
        return 1

    if eaten > n:
        return 0

    # Check cache to see if solution to part of cache has already
    # been calculated and stored.
    elif n in cache:
        return cache[n]

    else:
        cache[n] = eating_cookies_cached(n-3, cache) + eating_cookies_cached(n-2, cache) + eating_cookies_cached(n-1, cache)
        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")