'''
Input: an integer
Returns: an integer
'''

  #base case: all n cookies have been eaten. 
#   How many ways are there to eat 0 cookies? 0
#    What about a negative number of cookies? 0 

#make cache
#if find something in cache, just return the answer
#if not in cache continue with same logic.
def eating_cookies(n, cache=None):
    #base case: no more cookies
    total = 0
    if n == 0:
        #return 1 because this recursion will be valid
        return 1
    elif n < 0:
        return 0
    elif cache and cache[n] > 0:
        return cache[n]

    else:
        if not cache:
            #dictonary
            #cache = {i: 0 for i in range(n+1)}
            #list
            cache = [0 for _ in range(n+1)] 
        #we will save our answer to cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]
    # recursive case when there are still more cookies to be eaten
#    return eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    # make 3 recursive calls 

print(eating_cookies(5))
# def eat(method, n):
#     num_of_ways = 0
#     #for x to add up to n
#     #possible values
#     numbers=[i for i in range(0, n)]
    
#     for i in range(len(numbers)):
#         temp = 0
#         temp = numbers[i] + method

#         if temp == 3:
#             num_of_ways += 1



# print(eat(1, 3))

# def eating_cookies(n):
#     if n <= 0:
#         return 
#     # Your code here
#     methods = [1,2,3]
#     num_of_ways = 0

    
#     arr = []
#     eaten = sum(arr)

#     for i in len(methods):
#         eat(methods[i], n)
    
    # how many ways can 1,2,3 add up to 3
    #base case -> = 3
    # if eaten == 3:
    #     num_of_ways += 1 
    
    # return num_of_ways

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
