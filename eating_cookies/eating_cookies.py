'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # verify if exactly 0 cookies left
    if n == 0:
        # increment
        return 1
    # if a negative
    if n < 0:
        # do not increase/decrease combo count
        return 0
    # readme mentions a cache
    if cache is None:
        cache = {}
    elif isinstance(cache, list):
        cache = dict.fromkeys(cache)
    if n in cache:
        return cache[n]
    # if cookies are left in the jar
    #else:

        # try running through again with subtracting each type of input possibility
        #return eating_cookies(n-1, cache)+ eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    one_cookie = eating_cookies(n - 1, cache)
    two_cookies = eating_cookies(n - 2, cache)
    three_cookies = eating_cookies(n - 3, cache)
    
    cache[n] = one_cookie + two_cookies + three_cookies
    
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

eating_cookies(3)