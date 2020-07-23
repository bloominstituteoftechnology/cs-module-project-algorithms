def iterative_factorial(n):
    total, k = 1, 1

    while k <= n:
        total, k = total * k, k + 1

    return total


print(iterative_factorial(10))


def recursive_factorial(n):

    if n == 1:
        return 1

    else:
        return n * recursive_factorial(n-1)


print(recursive_factorial(10))
