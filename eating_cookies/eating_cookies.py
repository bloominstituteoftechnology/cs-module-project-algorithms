import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, memory=None):
    if memory == None:
        memory = [0] * (n + 1)
    if n <= 1:
        memory[n] = 1
    elif n == 2:
        memory[n] = 2
    elif memory[n] == 0:
        memory[n] = eating_cookies(n - 1, memory) + eating_cookies(n - 2, memory) + eating_cookies(n - 3, memory)
    return memory[n]
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    for i in range(10):
        num_cookies = i

        print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
