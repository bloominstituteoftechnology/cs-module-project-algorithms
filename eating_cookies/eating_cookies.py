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
    
# if n < 0:
#     return 
# if n == 0:
#     return 1

# else:
#    return  eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


# With the cache, every n value now is only computed once 
# The cache reduced the runtime from O(3^n) to O(n)
# We did increase space complexity 
def eating_cookies(n, cache):
    if n < 0:
        return 0
    if n == 0:
        return 1
    # check the cache to see if it holds the answer this branch is looking for 
    elif n in cache:
        return cache[n]
    else:
        # otherwise, n is not in the cache, so we need to compute the answer the "normal" way
        # once the answer is computed, save it in the cache 
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]
​
# how do we reduce the amount of redundant work? 
# use a data structure to "cache" (or "save") answers that some other branch has 
# already done 
# someone still has to figure out the answer in the first place 
# but once that answer is computed, we'll share that answer with any other branch
# that needs to calculate the same thing 
# branches that need an answer that's already been computed can check the cache 
# to see if the answer is already in there and just pull it out 
​
# what data structure should we use for the cache?
# save the n value for the branch along with its associated answer 
# save the n value as a key and the associated answer as its value in a dict 
# we'll need to pass the dict to each recursive call 
​
# Use the main function here to test out your implementation
num_cookies = 100
# cache = {i: 0 for i in range(num_cookies+1)}
print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to eat {num_cookies} cookies")
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
