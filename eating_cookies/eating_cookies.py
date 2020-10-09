'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     if n == 0 or n == 1:
#         return 1
#
#     if n == 2:
#         return 2
#
#     if n == 3:
#         return 4
#
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

### Optimization Time! Using Memoization (a cache to store)

def eating_cookies(n, cache=None):
    if n < 0: # check for negatives
        return 0 # this is not a solution

    if n == 0: # base case
        return 1 # getting to zero means finished

    if cache is None:
        cache = {} #instantiate cache

    if n in cache: # check for previous solutions
        return cache[n]

    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + \
                eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation

    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
