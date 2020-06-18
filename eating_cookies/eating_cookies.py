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
    if n <= 3:                           # ITERATIVE WORKING WITH BIG NUMBERS
        if n == 3:
            return 4
        elif n == 2:
            return 2
        elif n == 1:
            return 1
        else: 
            return 1
    else:
        back_3 = 1
        back_2 = 2
        back_1 = 4
        current = back_1 + back_2 + back_3
        counter = 4
        while counter < n:
            back_3 = back_2
            back_2 = back_1
            back_1 = current
            current = back_1 + back_2 + back_3
            counter += 1
    return current
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500


    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
