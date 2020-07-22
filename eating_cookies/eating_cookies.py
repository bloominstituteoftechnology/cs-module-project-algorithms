'''
Input: an integer
Returns: an integer
'''
from itertools import combinations
def eating_cookies(n):
    if n == 0:
        return 1
    elif n > 0 and n < 3:
        return n
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
