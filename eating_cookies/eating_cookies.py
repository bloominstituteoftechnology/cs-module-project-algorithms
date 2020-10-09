'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    eats = -1

    if n < 0:
        eats = 0
    elif n == 0:
        eats=1
    else:
        eats = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return eats

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
