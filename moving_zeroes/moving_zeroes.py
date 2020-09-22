'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Loop over the length of the array
    for i in range(len(arr)):
        # If the value at that index is 0
        if arr[i] == 0:
            # Create a new placeholder variable to hold that value
            zero = arr[i]
            # Remove that value from the array
            arr.remove(arr[i])
            # Insert the same value to the end of the array
            arr.insert((len(arr) + 1), zero)
    # Return the array after all loops run
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
