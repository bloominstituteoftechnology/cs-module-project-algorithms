# For reference:

def climb_stairs(current, desired):
    if current > desired:
        return 0
    if current == desired:
        return 1
    return climb_stairs(current+1, desired) + climb_stairs(current+2, desired)

'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    eaten = 0
    if eaten == n:
        return 1

    if eaten > n:
        return 0

    return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    print(climb_stairs(0, 5))

    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")