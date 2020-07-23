# FIRST-PASS:
def moving_zeroes(arr):
    '''
    Input: a List of integers
    Returns: a List of integers
    '''
    # Your code here

    mutated_arr = []

    # need to loop through array
    for i in arr:  # > O(n)

        # if 0, append to right side of array
        if i == 0:  # > O(1)
            mutated_arr.append(i)  # > O(1)

        # otherwise, add to left side
        else:
            mutated_arr = [i] + mutated_arr  # > O(k)
            # > `.insert()` alternative is O(n)

    return mutated_arr


def new_moving_zeroes(arr):

    # Is there a way I could do without for loop?
    # Could use counter, but would still be grabbing each value, so O(n)

    # Not quite clear if improvement is needed, bc current solution
    # has O(n * k) runtime and I do not know if that is better or
    # worse than O(n^2)


if __name__ == '__main__':
    # # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]

    # print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

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
