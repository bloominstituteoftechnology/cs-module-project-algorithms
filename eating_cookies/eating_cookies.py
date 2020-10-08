'''
Input: an integer
Returns: an integer

Cookie Monster can eat either 1, 2, or 3 cookies at a time.
'''


def eating_cookies(n, cache=None):
    print(n)

    ## add memoization
    

    # base cases
    if n == 0:
        return 1
    if n < 0:
        return 0
    # check if works has already been done by looking in the cache

    # is not None checks if the cache has been created
    # cache > 0 checkes if there's anything in it
    elif cache is not None and cache[n] > 0:
        # return the previously computed answer and don't recurse
        return cache[n]

    else:
        #create cache for the first time
        if cache is None:
            #initialize an empty list for a cache
            cache = [0 for i in range(n+1)]
        #store the value of the recursive call expressions in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    #recursion
    return cache[n]
    



'''
def eating_cookies(n):
    # Your code here

    ## use recursion

    ## base case
    #if cookies == 1 or 0


    ## add memoization
    d = {}
    

    if n == 0:
        ways_to_eat_cookies = 1
        return ways_to_eat_cookies

    elif n == 1:
        ways_to_eat_cookies = 1
        return ways_to_eat_cookies


    elif n ==2:
        ways_to_eat_cookies = 2
        return ways_to_eat_cookies

    elif n == 3:
        ways_to_eat_cookies = 4
        return ways_to_eat_cookies

    else:
        ## if you ate 1 cookie
        eat_one = eating_cookies(n-1)
        ## eat 2 cookies
        eat_two = eating_cookies(n-2)
        # eat 3 cookies
        eat_three = eating_cookies(n-3)


        ## almost there, but need to figure out the logic to look up if d[n] exists, and if so don't go through the recursion
        d[n] = eat_one+eat_two+eat_three
        print(d)

        return d[n]
'''






#ways_to_eat_cookies += 1

    #return ways_to_eat_cookies

            ##Try this: number of cookies / ways to eat
        # print((n//1)+(n//2)+(n//3)) NO


'''
3 
1 -> 2 -> 2
        1 ->1 
2 _> 1
3



n=4
1
    3
        
        2
        1
2
    2
3
    1

'''




    #what if it's 2 cookies?
    #eat 1 cookies 2x
    # eat 2 cookies 1x



    #what if it's 3 cookies?
    #eat 1 cookies 3x
    # eat 1 cookies 1x and 2 cookies 1x
    # eat 2 cookies 1x and 1 cookies 1x
    # eat 3 cookies 1x
    # elif n ==3:
    #     #1 + n-1 + 1

    #     3 2 1

    #     1
    #     1 1
    #     1

    #     n -1 n-1 until 1

    #what if it's 4 cookies?
    #eat 1 cookies 4x
    # eat 1 cookies 2x and 2 cookies 1x
    # eat 2 cookies 1x and 2 cookies 1x
    # eat 2 cookies 2x and 2 cookies 2 x
    # eat 3 cookies 1 x and 1 cookie 1x
    # eat 1 cookies 1 x and 3 cookie 1x
    # eat 4 cookies 1x



    # 5 cookies
'''
    1 cookie 5x
    1 c 3 x 2 c 1x
    2c 1x 1c 3x
    3c 1x 2c 1x

    5 c 1x


'''

    #return ways_to_eat_cookies


    #recursive function



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
