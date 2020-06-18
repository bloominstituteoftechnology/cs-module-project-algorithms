'''
Input: an integer
Returns: an integer
'''

### DAY 3: First Pass Solution ###
# def eating_cookies(n): # Naive recursive brute-force solution. O(3^n) time, O(3^n) space
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


### DAY 4: FUNCTION OPTIMIZED ###
def eating_cookies(n, cache=None):
    if n < 0: # check for negative values
        return 0 # getting to a negative number means we didn't find one of the ways
    if n == 0: # base case: when there are no more cookies
        return 1 # getting to 0, means we found a way to eat our cookies
    if cache is None: # if no cache yet
        cache = {} # create a cache
    if n in cache: # check for previosuly computed answer in our cache
        return cache[n] # return cache[n]
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) # this represents our recurive case, 3 possible decisions
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
