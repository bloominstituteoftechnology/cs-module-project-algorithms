'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    
    if n == 0:
        return 1
        # because there only one way to eat one cookie
    if n < 0:
        return 0
        # because there no way to eat no cookies
    if n >= 1:
        return eating_cookies(n-3)+eating_cookies(n-2)+eating_cookies(n-1)        
        # Applys the recurrsion part of problem, since we want a permutations
        
    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


print(f"There are {eating_cookies(cookies)} ways for Cookie Monster to each {cookies} cookies")