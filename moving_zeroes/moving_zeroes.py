"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(array):
    for x in range(len(array)):
        if array[x] != 0:
            non_zero = array.pop(x)
            array.insert(0, non_zero)
    return array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")