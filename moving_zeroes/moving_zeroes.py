'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # set the left index to 0 and the right index to the last value in the array
    left_index = 0
    right_index = len(arr) - 1

    # while the left index is not 0 and the left index is not the right index
    while arr[left_index] != 0 and left_index != right_index:
        #increment the left index by one
        left_index += 1

    # while the right index is equal to 0 and the right index is not the left index
    while arr[right_index] == 0 and right_index != left_index:
        # decrement the right index by 1
        right_index -= 1

    # while the left side is less than the right
    while left_index < right_index:
        # if the left index is 0 and the right is not 0
        if arr[left_index] == 0 and arr[right_index] != 0:
            # swap the position of the left and right indexes
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            
        #increment both indexes
        left_index += 1
        right_index -= 1
    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")