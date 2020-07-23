'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    print("\nRoot",n)
	
    if n < 0: # if less than 0, not possible
        print("1st",n)
        return 0
    elif n == 0: # if 0, end recursion
        print("2nd",n)
        return 1
    else:
        print("3rd",n)
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
