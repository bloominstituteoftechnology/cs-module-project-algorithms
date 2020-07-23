def fib(n, cache={}):

    if n<0:
        raise IndexError(
                'index was negative'
                'no such thing as a neg index in a series'
                )
    elif n in [0,1]:
        #base cases
        return n
    #cache
    elif n in cache:
        return cache[n]

    else:
        if cache is None:
            cache = {}
        
        cache[n] = fib(n-1, cache) + fib(n-2, cache)
    
    print("computing fib (%i)"%n)
    print(cache[n])
    return cache[n]

fib(100)