'''
Input: an integer
Returns: an integer
'''
def eating_cookies_naive(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies_naive(n-1) + eating_cookies_naive(n-2) + eating_cookies_naive(n-3)

def eating_cookies(n, cache=None):
    print(n)
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the work has already been done
    # by looking in the cache
    elif cache is not None and cache[n] > 0:
        #return the previosly computed answer and don't recurse
        return cache[n]
    else:
        # might need to create our cache for the first time
        if cache is None:
            cache = [0 for i in range(n+1)]
        # store the value of the recursive call expressions in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]

eating_cookies(20)
        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
