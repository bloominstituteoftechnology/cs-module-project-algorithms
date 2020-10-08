'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # 3 choices to eat cookies
#     # there is only one way to eat one cookie
#     if n < 0:
#         return 0
#     if n==0 :
#         return 1
#     else:
#        return  eating_cookies(n-1) + eating_cookies(n-2)+ eating_cookies(n-3)
# #there is a lot of redundant work in first solution
# use datastructure to cache(or save) the answer that has already calculated 
# by other branches
#what datastructure should we use for the cache?
#save the n value and answer associated with the n value
#we need to pass the cache the dictionary to the recursive call
# to access as well as update the cache

#with cache every n value computed once
# the cache reduce the runtime from O( 3^n) to O(n)

def eating_cookies(n, cache):
    # 3 choices to eat cookies
    # there is only one way to eat one cookie
    if n < 0:
        return 0
    if n==0 :
        return 1
        #check the cache to see if it holds the answer for the branch
    elif n  in cache:
        return cache[n]

    else:
       #otherwise, n is not in the cache, so we need to calculate the anwser for the branch
       #save the answer in the cache
       cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-3, cache)
       return cache[n]







if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
