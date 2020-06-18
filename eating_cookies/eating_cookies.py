'''
Input: an integer
Returns: an integer
'''

# def eating_cookies(n):
#     # This problem is similar to the ways to climb the stairs problem
#     # Since we are dealing with permutations, recursion is well suited
#     # However, as the instructions note, the performance will be poor, with exponential runtime

#     # One base case will check if there are zero cookies left, if so that counts as a way
#     # The other base case is if there are negative cookies left, if so that does not count as a way
#     # Then we just return the sum of the possibilities of eating cookies 1, 2, or 3 at a time
    
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0

#     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

def eating_cookies(n, cache):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]
        
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
