'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    value = 0
    n_1 = 1
    n_2 = 1
    n_3 = 0
    for i in range(n-1):
        value = n_1 + n_2 + n_3
        n_3 = n_2
        n_2 = n_1
        n_1=value
    return value

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
