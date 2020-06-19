'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n):
    '''
    if n <= 3:                    # RECURSIVE ISNT GOOD WITH BIG NUMBERS
        if n == 3:
            return 4
        elif n == 2:
            return 2
        elif n == 1:
            return 1
        else: 
            return 1
    else:
        total = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)  
    return total
    '''
    # ITERATIVE WORKING WITH BIG NUMBERS
    if n <= 3:                           # return cases where n is 0,1,2,3
        if n == 3:
            return 4
        elif n == 2:
            return 2
        elif n == 1:
            return 1
        elif n == 0: 
            return 1
        else: 
            return 0
    else:                               # if n is 4 or more 
        back_3 = 1             # back_3 is f(n-3) in this case f(4-3) = f(1) = 1
        back_2 = 2              # back_2 = f(4-2) = f(2) = 2
        back_1 = 4                # back_1 = f(4-1) = f(3) = 4
        current = back_1 + back_2 + back_3    # calculate f(4) = f(3) + f(2) + f(1)
        counter = 4                         
        while counter < n:                  # move everything up until counter = n
            back_3 = back_2
            back_2 = back_1                 #switching all up 1
            back_1 = current
            current = back_1 + back_2 + back_3      # calculate for the next step
            counter += 1
    return current

'''
#CACHE WAY
def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0: 
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1,cache)
    return cache[n]
'''



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500
    #cache = {i: 0 for i in range(num_cookies+1)}

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
