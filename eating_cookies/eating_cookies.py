# from scipy.special import comb

def eating_cookies(n):
    '''
    Input: an integer (number of cookies in jar)
    Returns: an integer (number of ways cookie monster can eat the cookies in jar)
    '''
    # Your code here

    # will need to count the ways monster can eat

    # different ways to eat
    k1 = n - 1
    k2 = n - 2
    k3 = n - 3

    # will need to keep track of results for base case
    # can try memoization
    # (https://www.geeksforgeeks.org/memoization-using-decorators-in-python/)
    memory = {}

    # base case - n is in memory
    if n in memory:
        return memory[n]

    # otherwise, handle the ex. case first

    # > got `max recursion depth exceeded` error on this structure:
    # else:
        # if n == 0:
        # etc ...
    # > so changed to:

    # if none
    elif n == 0:
        ways = 1  # > test is looking for 1, but how does monster eat 0 cookies?
    # if one
    elif n == 1:
        ways = 1
    # if two
    elif n == 2:
        ways = 2
    # if three
    elif n == 3:
        ways = 4
    # if more than 3
    else:
        # try recursion - call `eating_cookies` on all the ways to eat
        # each call should return number of options
        ways = eating_cookies(k1) + eating_cookies(k2) + eating_cookies(k3)

    # get closer to base case
    memory[n] = ways

    return ways


if __name__ == "__main__":
    # # Use the main function here to test out your implementation
    # num_cookies = 5

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    # `eating_cookies(3)` should return an answer of 4.

    # print(comb(5,3))

    # k1 = 1
    # k2 = 2
    # k3 = 3

    print(eating_cookies(10))  # > 274
