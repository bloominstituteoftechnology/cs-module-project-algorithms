def fib(n, cache={}):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n in [0, 1]:
        # Base cases
        cache[0], cache[1] = 1, 1

    if n in cache:
        return cache[n]

    print("computing fib(%i)" % n)

    cache[n] = fib(n - 1) + fib(n - 2)

    return cache[n]


fib(30)
