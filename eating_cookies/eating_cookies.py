'''
Input: an integer
Returns: an integer
'''
def sub(n):
    # callback, check if even (1 way) or under (0 ways)
    w = 0 # ways to eat cookies
    if n == 0:
        return 1
    if n < 0:
        return 0

    # check if more cookies can be eaten, recurse
    if n > 2:
        w += sub(n-3)
    if n > 1:
        w += sub(n-2)
    if n > 0:
        w += sub(n-1)
    
    return w

# call function, runs when eating_cookies is called
def eating_cookies(n, arr=None):
    # check if array isn't given and run just the recursion
    if arr is None:
        return sub(n)

    # otherwise use the faster, mathematical method
    for i in range(3): # set up the pattern
        arr[i] = eating_cookies(i+1)
    
    # use math to get the rest of the way there
    for i in range(3, len(arr) - 1):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

    return arr[-2]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_ways = []
    for n in range(1,16):
        num_ways.append(eating_cookies(n))
    
    print(num_ways)