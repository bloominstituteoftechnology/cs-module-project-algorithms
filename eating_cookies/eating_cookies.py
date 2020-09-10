'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # BASE CASE: If cookies eaten is more than n return 0
    eaten = 0
    if eaten > n:
        return 0
    # If eaten is the number of available cookies, return a count of 1
    if eaten == n:
        return 1

    # Else, use recursion to loop through each potential options incrementing eaten by potential options
    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")