def factorial(n):

    #base case
    #we know the answer of 0 factorial, its 1
    if n == 0:
        return 1
    # we know that n factorial is n * n-1 factorial
    return n * factorial(n-1)

#print(factorial(5))

#recursion starts calculating at base case
#another example
def get_recursive_fact(n):
    #if n is less 0 return error
    if n < 0:
        return -1
    #base case
    elif n < 2:
        return 1
    else:
        return n * get_recursive_fact(n-1)
print(get_recursive_fact(5))

#vs loop

def inter_fact(n):
    value = 1
    #range does not include final number
    for i in range(1, n+1):
        value *= i
    return value

#print(inter_fact(5))

# fibonacci
# takes its value and adds it to the value
#before it
# 1,1,2,3,5,8,13....
cache = {}

def fib(n):
    # if n in fib cache, return n
    print('cache', cache)
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
    return n + fib(n-1) 
    
#print(fib(5))
 

for n in range(1, 101):
    print(n, ':', fib(n))