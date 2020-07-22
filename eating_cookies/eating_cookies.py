"""
Input: an integer
Returns: an integer
"""


# Cookie Monster can eat 1, 2, or 3 cookies at once
# a jar with an unknown number inside, how many can be eaten
def eating_cookies(n):
    # Your code here
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
