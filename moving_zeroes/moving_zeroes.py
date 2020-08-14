'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # if it's not a zero, move it to index self.index - 1
    # or hold index of zero in a variable so that the number is moved to (index of zero) - 1
    # or move zeros to the right and ignore non zero numbers
    # if not zero, swap with last zero

    count_zero = arr.count(0)
    while 0 in arr:
        arr.remove(0)
    for n in range(count_zero):
        arr.append(0)
    return arr

    for i in range(len(arr)):
        if arr[i] == 0:
            zero_idx_array.append(i)
    for z in zero_idx_array:
        for n in range(len(arr))
    """
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    #arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]
    #arr = [0, 0, 1, 0, -2]

    print(f"The result of moving_zeroes is: {moving_zeroes(arr)}")