"""
Algorithms, problem 1.
"""

def single_number(arr):
    """
    Input: a list of integers where every int except one shows up twice
    Returns: an integer
    """

    singletons = set()

    for num in arr:
        if num in singletons:
            # A duplicate occurrence of a previously encountered number.
            # (Actually any even occurrence, but input restrictions make this
            # okay.)
            singletons.remove(num)
        else:
            # The first occurrence of a number in the array.
            # (As above, actually any odd occurence.)
            singletons.add(num)

    return singletons.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    test_arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(test_arr)}")
