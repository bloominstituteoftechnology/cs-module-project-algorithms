'''
Input: an integer
Returns: an integer
'''

# Caching/Memoization: Save your work so you don't have to repeat it again
# Need some sort of data structure to save the data
# arrays and dictionaries
# if we check cache and see the answer we are looking for is in there
# return our answer
# if the cache doesn't have our answer
# how do we get answers in there?
# The first time we calculate an answer
# 

def eating_cookies(n, cache = None):

    # first pass solution in class
    # base case no more cookies
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # init the cache if we don't have it yet
    # add a case to check the cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i:0 for i in range(n+1)}
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]
    
    

    # yesterday's homework solution
    # if n < 0:
    #     pass
    # elif n == 0:
    #     return 1
    # if n == 1 or n == 2:
    #     return n
    # elif n == 3:
    #     return 4
    # else:
    #     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    # expected = 13

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
