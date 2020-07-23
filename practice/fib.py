0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fib(n, cache = {}):
  if n < 0:

    raise IndexError('Index was negative. No such thing as negative in a series.')

  elif n in [0, 1]:
    #base cases

    return n

  elif n in cache:
    print('grabbing from cache[%i]' % n)
    
  
  print('computing fib(%i' % n)
  cache[n] = fib(n-1) + fib(n - 2)
  return fib(n - 1) + fib(n - 2)
  return cache[n]
fib(4)