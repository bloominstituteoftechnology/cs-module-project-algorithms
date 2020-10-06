'''
Input: an integer
Returns: an integer
'''

# First Pass Solution

# def eating_cookies(n):
#     # Your code here
#     if n <= 0:
#         return 1
#     if n is 1:
#         return 1
#     if n is 2:
#         return 2
#     if n is 3:
#         return 4

#     one_cookie = eating_cookies(n - 1)
#     two_cookies = eating_cookies(n - 2)
#     three_cookies = eating_cookies(n - 3)
#     return one_cookie + two_cookies + three_cookies

# Second Pass Solution

# results = {}

# def eating_cookies(n):
#     # Your code here
#     if n <= 0:
#         return 1
#     if n is 1:
#         return 1
#     if n is 2:
#         return 2
#     if n is 3:
#         return 4
#     if n in results.keys():
#         return results[n]
#     one_cookie = eating_cookies(n - 1)
#     two_cookies = eating_cookies(n - 2)
#     three_cookies = eating_cookies(n - 3)
#     if n not in results.keys():
#         results[n] = one_cookie + two_cookies + three_cookies
#         return one_cookie + two_cookies + three_cookies

# From Lecture Optimized Solution

def eating_cookies(n, cache=None):
    # Your code here
    if n < 0:
        return 0
    if n is 0:
        return 1

    if cache is None:
        cache = {}
    elif isinstance(cache, list):
        cache = dict.fromkeys(cache)
    if n in cache:
        return cache[n]
    one_cookie = eating_cookies(n - 1, cache)
    two_cookies = eating_cookies(n - 2, cache)
    three_cookies = eating_cookies(n - 3, cache)

    cache[n] = one_cookie + two_cookies + three_cookies
    
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50
    
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
