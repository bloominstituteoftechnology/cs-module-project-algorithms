'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

def eating_cookies(n, cache = None):
    # Check for negative values
    if n < 0:
    # Getting to a negative number means we didn't find one of the ways
        return 0
    # Base case when there are no more cookies to find
    if n == 0: 
    # Getting to 0 means we found a way to eat our cookies
        return 1
    # If no cache yet
    if cache is None:
    # Creating a cache
        cache = {} 
    # Check for previosuly computed answer for our cache
    if n in cache:
    # Return cache[n]
        return cache[n] 
    cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
