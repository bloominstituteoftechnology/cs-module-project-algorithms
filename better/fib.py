import time

def calc_time():
    print(f"\nResult calculated in {time.time() - start:.5f} seconds")
    print("\n============================")

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# start = time.time()
# print(fib(30))
# calc_time()

# memoizaiton - dp
# top down approach

def memo_fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = memo_fib(n-1, memo) + memo_fib(n-2, memo)
    return memo[n]

# start = time.time()
# print(memo_fib(30))
# calc_time()

# tabulation - dp
# bottom up approach
# no recursion needed

def constant_tab_fib(n):
    prev1 = 0
    prev2 = 1
    curr = 0
    for _ in range(0, n):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return curr

print(constant_tab_fib(5))

def tab_fib(n):
    # underscore _ is to denote not using var in iteration
    table = [0 for _ in range(0, n+1)]
    table[0] = 1
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(tab_fib(5))