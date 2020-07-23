'''
Input: an integer
Returns: an integer
'''


def eating_cookies(numberOfCookies, cache=None):
    # base case
    if numberOfCookies == 0:
        return 1
    elif numberOfCookies < 0:
        return 0
    # check if the work has already been done
    # by looking in the cache
    elif cache is not None and cache[numberOfCookies] > 0:
        # return the previously computed answer and don't recurse
        return cache[numberOfCookies]
    else:
        # might need to create our cache for the first time
        if cache is None:
            # initialize an empty list for a cache
            cache = [0 for i in range(numberOfCookies + 1)]
            # store the value of the recursive call expression in out cache
        cache[numberOfCookies] = eating_cookies(numberOfCookies - 1, cache) + eating_cookies(numberOfCookies - 2, cache) + eating_cookies(numberOfCookies - 3, cache)

    return cache[numberOfCookies]

"""
In order to show the redundant work going on, add a print(n) statement at the beginning of eating cookies
and run with a decent sized input.
"""
"""
After discussing how to use a cache in theory in LucidChart,now, make that a reality in the code here.
"""


"""
SPRINT Challenge Need to know:
- Selection sort or bubble sort
- Using recursion to solve a code challenge
- Determine the time complexity of given code (including recognizing O(log n))
- Recognizing where you can get O(log n) by using binary search
"""


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
