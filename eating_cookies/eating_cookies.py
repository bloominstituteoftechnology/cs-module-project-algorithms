from scipy.special import comb

def eating_cookies(n):
    '''
    Input: an integer (number of cookies in jar)
    Returns: an integer (number of ways cookie monster can eat the cookies in jar)
    '''
    # Your code here
    # TODO

    # will need to count the ways monster can eat
    ways = 0

    # if only 1 cookie in jar, only one way to eat all of the cookies
    if n == 1:
        ways += 1
        return ways

    if n > 1:
        # eating 1 cookie at a time should always be an option
        return 
    

if __name__ == "__main__":
    # # Use the main function here to test out your implementation
    # num_cookies = 5

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    # `eating_cookies(3)` should return an answer of 4.

    print(comb(5,3))

    k1 = 1
    k2 = 2
    k3 = 3
   