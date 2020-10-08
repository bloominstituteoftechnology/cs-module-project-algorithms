'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    # Your code here

    #pass
    
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-1, cache) 
    return cache[n]

    # prev1, prev2, prev3 = 1, 1, 0
    # combinations = 1
    # for i in range (1, n):
    #     combinations = prev1 + prev2 + prev3
    #     prev3, prev2, prev1 = prev2, prev1, combinations
    # return combinations





if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cache = {i: 0 for i in range(num_cookies+1)}

    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")
