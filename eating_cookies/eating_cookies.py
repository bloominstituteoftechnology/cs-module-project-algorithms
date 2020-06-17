'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # base case
    if n<0:
        return 0
    elif n == 0:
        return 1
    # if only 1 cookie
    elif n==1:
        return 1
    # if two cookies:
    elif n==2:
        return 2
    # if three or more cookies:
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = -1

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
