'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    num_zeros = arr.count(0)

    arr_without_zeros = [i for i in arr if i != 0]
    new_array_with_zeros = [0] * num_zeros

    moved_zeros = arr_without_zeros + new_array_with_zeros

    return moved_zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


def moving_zeroes_2(arr):
    pass
