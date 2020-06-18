'''
Input: an integer
Returns: an integer
'''
# My first-pass solution
# def eating_cookies(n):
#     # base case
#     if n<0:
#         return 0
#     elif n == 0:
#         return 1
#     # if only 1 cookie
#     elif n==1:
#         return 1
#     # if two cookies:
#     elif n==2:
#         return 2
#     # if three or more cookies:
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# Optimized solution
def eating_cookies(n, cache=None):
    # check for negative values
    if n < 0:
        # getting to a negative number means we didn't find one of the ways
        return 0
    # base case: when there are no more cookies
    if n == 0:
        # getting to zero means we find a way to eat our cookies
        return 1
    
    # if no cache yet, create one
    if not cache:
        cache = {}
    
    # check for previously computer answer in or cache
    if n in cache:
        return cache[n]
    
    # this represents our recursive case
    # three possible decisions
    # eat 1 cookie, 2 cookies, or 3 cookies
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
