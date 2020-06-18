'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    #base case: when there are no more cookies
    if n == 0:
        # we found a way to eat our cookies
        return 1
    # check for negative values
    if n < 0:
        # this is not a valid way to eat our cookies
        return 0

    # this represents our recurive case
    # 3 possible decisions
    # eat 1 cookie, 2 cookies, or 3 cookies
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
