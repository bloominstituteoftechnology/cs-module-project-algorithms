'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # assign empty array to non_zero list
    temp = [0] * len(arr) 
    # initialize index of arr and temp
    i = j = 0
    # iterate through array
    while i < len(arr):
        # if i is not 0
        if arr[i] != 0:
            # assign value from arr to temp
            temp[j] = arr[i]
            # increment index for temp
            j += 1
        # increment index for arr
        i += 1
    # loop through temp and update arr with value from temp
    for i in range(0, len(temp)):
        arr[i] = temp[i]
    # return mutated arr
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")