'''
  Input: an integer
  Returns: an integer
  '''


def eating_cookies(n, memory=None):
    cookies = n

    # we check if memory == None

    if memory == None:

        # if memory == None set it to a list with [0] and multiply that by cookies + 1 (This still just gives us an empty list of 0 but 5 times (one for each cookie))

        memory = [0] * (n + 1)

    # if cookies is less than or equal to 1

    if cookies <= 1:

        # set memory[cookies] = 1.

        memory[cookies] = 1

    # if cookies is less than or equal to 2

    elif cookies == 2:

        # set memory[cookies] = 2.

        memory[cookies] = 2

    # the memory of cookies is 0

    elif memory[cookies] == 0:
        memory[cookies] = eating_cookies(cookies - 1, memory) + eating_cookies(
            cookies - 2, memory) + eating_cookies(cookies - 3, memory)
    return memory[cookies]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
