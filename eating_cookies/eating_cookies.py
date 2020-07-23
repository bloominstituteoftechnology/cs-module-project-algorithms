### FIRST PASS:

# def eating_cookies(n):
#     '''
#     Input: an integer (number of cookies in jar)
#     Returns: an integer (number of ways cookie monster can eat the cookies in jar)
#     '''
#     # Your code here

#     # will need to count the ways monster can eat

#     # different ways to eat
#     k1 = n - 1
#     k2 = n - 2
#     k3 = n - 3

#     # will need to keep track of results for base case
#     # can try memoization
#     # (https://www.geeksforgeeks.org/memoization-using-decorators-in-python/)
#     memory = {}

#     # base case - n is in memory
#     if n in memory:
#         return memory[n]

#     # otherwise, handle the ex. case first

#     # > got `max recursion depth exceeded` error on this structure:
#     # else:
#         # if n == 0:
#         # etc ...
#     # > so changed to:

#     # if none
#     elif n == 0:
#         ways = 1  # > test is looking for 1, but how does monster eat 0 cookies?
#     # if one
#     elif n == 1:
#         ways = 1
#     # if two
#     elif n == 2:
#         ways = 2
#     # if three
#     elif n == 3:
#         ways = 4
#     # if more than 3
#     else:
#         # try recursion - call `eating_cookies` on all the ways to eat
#         # each call should return number of options
#         ways = eating_cookies(k1) + eating_cookies(k2) + eating_cookies(k3)

#     # get closer to base case
#     memory[n] = ways

#     return ways

# Implementation has O(3^n) runtime complexity due to the fact that there
# are three possible decisions each time



### OPTIMIZED SOLUTION:

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



if __name__ == "__main__":
    # # Use the main function here to test out your implementation
    # num_cookies = 5

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    # `eating_cookies(3)` should return an answer of 4.

    # print(comb(5,3))

    # k1 = 1
    # k2 = 2
    # k3 = 3

    print(eating_cookies(500, {}))  # > 274
