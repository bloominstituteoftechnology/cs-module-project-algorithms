"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    """
    Cookie Monster can eat either 1, 2, or 3 cookies at a time
    Implement a function eating_cookies that counts the number of possible ways Cookie Monster
    can eat all of the cookies in the jar.
    """
    # Plan: Use Recursion until you hit the base cases
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    if n <= 0:
        return 1
    if n > 3:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
