'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    
    num_cookies = n
    counter = 0

    # base cases
    if num_cookies <= 0:
        # return 'There are no cookies in the cookie jar'
        return counter
        
    if num_cookies == 1:
        return counter + 1

    if num_cookies == 2:
        return counter + 2

    if num_cookies == 3:
        return counter + 4

    # Jenn's psuedo code starts here
    # Can only eat 3 cookies max at a time 

    # if num_cookies > 3:
        #if num_cookies % 3 = 1:
            #


    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
