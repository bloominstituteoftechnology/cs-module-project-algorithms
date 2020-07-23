'''
Input: an integer
Returns: an integer

Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

'''
# if n = 0 then return 1
# if n = 1 then return 1
# if n = 2 then return 2
# if n = 3 then return 4

# def eating_cookies(num_cookies): 
#     n = num_cookies
#     if n == 1 or n == 0:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


# def eating_cookies(num_cookies, var=None):
    
#     n = num_cookies  
#     result_array = [0] * (n+1)
    
#     # base cases:
#     if n == 0:
#         return 1

#     if n == 1:
#         return 1
    
#     result_array[0] = 1
#     result_array[1] = 1
#     result_array[2] = 2

#     for i in range(3, n+1):
#         result_array[i] = result_array[i-1]+result_array[i-2]+result_array[i-3]
    
#     return result_array[n]

def eating_cookies(n, cache=None):  # Note: the default value is used when function is first initialized, not every time called.

# check whether we have a cache, if not create one.
    if cache is None:
        cache = {}
    
    # base cases
    # n==0 means we found a way to eat our cookies.
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    # if we have a cache and already have a value in the cache for n, return it.
    if cache and cache[n]:
        return cache[n]
    # if we don't have a value in the cache for n, calculate the value and store it.
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    # return the cache for n
    return cache[n]




# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
