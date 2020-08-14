'''
Input: an integer
Returns: an integer
Cookie Monster can eat either 1, 2, or 3 cookies at a time. 
If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? 
Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 
'''
def eating_cookies(n, cache=None):
    if cache is None:
        cache = {}
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    if cache and cache[n]:
        return cache[n]

    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

     

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
