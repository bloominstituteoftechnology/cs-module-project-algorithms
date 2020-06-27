# fibonacci
# takes its value and adds it to the value
#before it
# 1,1,2,3,5,8,13....
cache = {}

def fib(n):
    # if n in fib cache, return n
    if n in cache:
        return cache[n]
    #base case 
    if n == 1:
        # return first term
        value = 1
    elif n == 2:
        #return second term
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)

    #cache value and return it
    cache[n] = value
    return value 
    

for n in range(1, 101):
    print(n, ':', fib(n))