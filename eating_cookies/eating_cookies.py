'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):

    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    # num_combos = 1  # 1 cookie at a time

    # # how many combos of 3's
    # if n % 3 == 0:
    #     num_combos += 1
    #
    # # how many combos of 2's
    # if n % 2 == 0:
    #     num_combos += 1
    #
    # # how many combos of all 1's and a 2
    # if n - 2 > 0:
    #     num_combos += (n - 2) + 1
    #
    # # how many combos of all 1's and a 3
    # if n - 3 > 0:
    #     num_combos += (n - 3) + 1







    return num_combos

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
