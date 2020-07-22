'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    mutated_arr = []
    # need to loop through array
    for i in arr:
        # if 0, append to right side of array
        if i == 0:
            mutated_arr.append(i)
        # otherwise, add to left side
        else:
            mutated_arr = [i] + mutated_arr

    return mutated_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

    # Examples
    # ```
    # Sample input: [0, 3, 1, 0, -2]
    # Expected output: 3
    # Expected output array state: [3, 1, -2, 0, 0]
    # ```

    # ```
    # Sample input: [4, 2, 1, 5]
    # Expected output: 4
    # Expected output array state: [4, 2, 1, 5]
    # ```

    # l = [1,2,3,4]

    # l = [5] + l
    # print(l)

    samp = [0, 3, 1, 0, -2]
    samp = moving_zeroes(samp)
    print(samp)
