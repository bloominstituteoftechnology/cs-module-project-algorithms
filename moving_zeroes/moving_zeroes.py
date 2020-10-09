def moving_zeroes(arr):
    """
    Write a function that takes an array of integers and moves each non-zero integer
     to the left side of the array, then returns the altered array.
     The order of the non-zero integers does not matter in the mutated array.
     Input: a List of integers
    Returns: a List of integers
    """
    # so could append to the end if it equals zero
    for i in arr:
        if i == 0:
            # remove so that we don't have leftover zeroes
            arr.remove(i)
            arr.append(i)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")