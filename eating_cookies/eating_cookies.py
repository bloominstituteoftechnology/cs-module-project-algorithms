'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        pass
    elif n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    # expected = 13

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
