"""
Algorithms, problem 5
"""

def eating_cookies(n, cache=None):
    """
    Input: an integer
    Returns: an integer
    """

    # It's like the Fibonacci sequence, but summing the previous three elements
    # instead of the previous two.
    if n > 2:
        ancestors = [1, 1, 2]
        for _ in range(n - 2):
            ancestors.append(sum(ancestors))
            ancestors.pop(0)
        return ancestors[2]

    # Base cases, n <= 2.
    if n == 2:
        return 2
    return 1

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster "
          f"to eat {num_cookies} cookies.")
