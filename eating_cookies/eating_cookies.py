'''
Input: an integer
Returns: an integer
'''

# keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# values = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927]
# results = dict(zip(keys, values))
results = {}

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

def eating_cookies(n):
    # Your code here
    if n <= 0:
        return 1
    if n is 1:
        return 1
    if n is 2:
        return 2
    if n is 3:
        return 4
    if n in results.keys():
        return results[n]
    one_cookie = eating_cookies(n - 1)
    two_cookies = eating_cookies(n - 2)
    three_cookies = eating_cookies(n - 3)
    if n not in results.keys():
        results[n] = one_cookie + two_cookies + three_cookies
        return one_cookie + two_cookies + three_cookies

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50
    
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
