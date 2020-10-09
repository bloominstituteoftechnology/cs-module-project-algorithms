'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    # Your code here
    if n < 0:
        return 0
    
    if n == 0:
        cache[0] = 1
        return 1
    
    if n in cache:
        return cache[n]
    
    result_n_1 = eating_cookies(n-1, cache)
    result_n_2 = eating_cookies(n-2, cache)
    result_n_3 = eating_cookies(n-3, cache)
    result_at_n = result_n_1 + result_n_2 + result_n_3
    
    cache[n] = result_at_n
    
    return result_at_n

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to eat {num_cookies} cookies")
