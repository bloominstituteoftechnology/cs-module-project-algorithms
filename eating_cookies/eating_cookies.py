'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    amount = 1
    for x in range(0, n+1):
        print(x)
    # return amount


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
