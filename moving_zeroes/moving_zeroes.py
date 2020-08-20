'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # check to see if you are not a zero
    cur_index = 0
    zero_count = 0
    while cur_index < len(arr):
        if arr[cur_index] != 0:
            # count how many zeros you have passed
            swap_index = cur_index - zero_count
            # swap between that zero and where you are not a zero
            arr[swap_index], arr[cur_index] = arr[cur_index], arr[swap_index]
        else:
            zero_count += 1

        cur_index += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")