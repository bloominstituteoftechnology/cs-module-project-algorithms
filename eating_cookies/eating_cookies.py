'''
Input: an integer
Returns: an integer
'''
def eating_cookies(desired):
    # recursive 
    # cookie monster can eat 1, 2, 3 cookies at a time
    current = desired
    if current > desired:
        return 0
    if current == desired:
        return 1

    else: 
        current += 1

    return eating_cookies(desired) + eating_cookies(desired) + eating_cookies(desired)
    
ok = eating_cookies(5)
print(ok)
    

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
