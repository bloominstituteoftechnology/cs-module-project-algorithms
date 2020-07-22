'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    cache = {}

    if n in cache:
        return cache[n]

    elif n <= 0:
        result = 1

    elif n == 1:
        result = 1

    elif n == 2:
        result = 2

    elif n == 3:
        result = 4

    else:
        result = eating_cookies(
            n-3) + eating_cookies(n-2) + eating_cookies(n-1)

    cache[n] = result

    return result


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

print(eating_cookies(10))
