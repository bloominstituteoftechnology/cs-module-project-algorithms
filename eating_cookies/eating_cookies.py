'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    #represents possibilty that are invalid possibility - because result = negative number(if there is no cookies left to be = 0)
    if n < 0:
        return 0
# when we can take 1 possibility to take that amount of cookies
    elif n == 0:
        # 1 possibility to eat them all
        return 1
    else:
        return eating_cookies(n - 1) + eating_cookies( n - 2) + eating_cookies(n - 3)
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
