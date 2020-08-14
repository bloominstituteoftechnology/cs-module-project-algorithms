'''
Input: an integer
Returns: an integer
'''




# def eating_cookies(n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     # doing the recursion portion of the function
#     num = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#     return num



# making the inner function that will be called from the eating_cookies function
def memo_eat_cookies(n, cookieArray):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if cookieArray[n] == 0: # should not get here with a n of 0 becuase will exit with the 
                            # above return statement
        cookieArray[n] = memo_eat_cookies(n-1, cookieArray) + memo_eat_cookies(n-2, cookieArray) + memo_eat_cookies(n-3, cookieArray)
    return cookieArray[n]



# This is the second pass of the method using memoization
# This is the wrapper function that will be used to setup and then call the 
# recursize function
# def eating_cookies(n,):
#     # setting up the array that will be passed into the
#     # inner function
#     arr = [0 for _ in range(n+1)]

#     return memo_eat_cookies(n, arr)
    

# Trying to do it a way that is from the bottom up
def eating_cookies(n):
    if n < 2:
        return 1
    if n == 2:
        return 2

    # making the table 
    table = [0] * (n +1)
    # filling in the first few of 
    table[0] = 0
    table[1] = 1
    table[2] = 2
    table[3] = 4
    # doing the looping to build the table
    for i in range(4, len(table)):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    return table[n]



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
