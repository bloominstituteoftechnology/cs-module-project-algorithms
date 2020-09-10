'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache={}):
    ''' FIRST PASS SOLUTION '''

    # # BASE CASE: If n is less than 0, return a count of 0
    # if 0 > n:
    #     return 0

    # # If n is 0, return a count of 1
    # if n == 0:
    #     return 1

    # # Else, use recursion to loop through each potential options incrementing eaten by potential options
    # return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    ''' WRITING BETTER SOLUTIONS '''

    # Use cache for memoization of recursive calls to the method
    # If cache is empty, set it to be a range
    if not cache:
        cache = [0 for i in range(n + 1)]

    # BASE CASE: If n is less than 0, return a count of 0
    if 0 > n:
        return 0

    # If n is 0, return a count of 1
    if n == 0:
        cache[n] = 1

    # If n not in cache, use recursion to loop through each potential options and storing to the cache
    if cache[n] == 0:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")