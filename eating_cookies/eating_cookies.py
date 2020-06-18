'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, useless_param=None):
    return eating_cookies_helper(n, 0, {})

def eating_cookies_helper(n, curr, cache):
    if curr in cache:
        return cache[curr]
    diff = n - curr
    solution_count = 0
    if diff == 0:
        return 1
    if diff >= 3:
        result = eating_cookies_helper(n, curr+3, cache)
        cache[curr+3] = result
        solution_count += result
    if diff >= 2:
        result = eating_cookies_helper(n, curr+2, cache)
        cache[curr+2] = result
        solution_count += result
    if diff >= 1:
        result = eating_cookies_helper(n, curr+1, cache)
        cache[curr+1] = result
        solution_count += result
    cache[curr] = solution_count
    return solution_count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 1

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
