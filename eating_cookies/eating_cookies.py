'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # check if there are cookies in the jar
    if n < 0:
        return 0

    # if value is 0 there is only one way of eating the cookies
    elif n == 0:
        return 1
    
    else: 
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)



    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
