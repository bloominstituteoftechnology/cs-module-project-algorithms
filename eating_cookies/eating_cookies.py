'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n, cache={}):
#     if n in cache:
#         return cache[n]
#     elif n <0:
#         return 0
#     elif n <1:
#         return 1
#     elif n ==2:
#         return 2 
#     else:
#         cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
#     return cache[n]



def eating_cookies(n, cache={}):
     #base case
     if n == 0:
         return 1
     elif n< 0:
         return 0
     else:
         #make 3 recursive calls
         return eating_cookies(n-1) +eating_cookies(n-2)+eating_cookies(n-3)
     
     
     
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    
    
 