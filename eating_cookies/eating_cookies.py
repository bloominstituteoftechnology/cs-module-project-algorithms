'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # check if there are cookies in the jar
#     if n < 0:
#         return 0

#     # if value is 0 there is only one way of eating the cookies
#     elif n == 0:
#         return 1
    
#     else: 
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    # here the computation is O(2**n) time complexity

    # implementing memoization and using cache allows work to be save
    # cache is a dictionary where keys is the n, value is the answer
def eating_cookies(n, cache): 
    # reduces runtime down to O(n)
    # if value is negative, return 0
    if n < 0:
        return 0
    # if value is 0, there's only one way of eating the cookies
    elif n == 0:
        return 1
    # utilizing the cache, check if the answer is in there
    elif cache[n] > 0:
        return cache[n]
    # if it hasn't been done yet and isn't in cache, use recursion and save it in cache
    else:
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)

    return cache[n]
    




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 99
    cache = {i: 0 for i in range(num_cookies + 1)}
    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies")
