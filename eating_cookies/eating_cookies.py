'''
Input: an integer
Returns: an integer
'''
def eating_cookies(cookies, cache = []):
    # construct cache
    if len(cache) is 0:
        cache = [0] * (cookies + 1)
    # Number of cookies is less thn 0 , return 0
    if cookies < 0:
        return 0
    # Number of cookies is less or equal to 1, return 1
    elif cookies <= 1:
        return 1
    # get combinations from cache
    elif cache[cookies]>0:
        return cache[cookies]
    else:
        # calculate number of combinations
        result = eating_cookies(cookies - 3, cache) + eating_cookies(cookies - 2, cache) + eating_cookies(cookies - 1, cache)
        cache[cookies] = result
        return result
        
        


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
