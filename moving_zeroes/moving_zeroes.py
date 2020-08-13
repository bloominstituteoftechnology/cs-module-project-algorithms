''''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # The count of non-zero elements
    count = 0

    # if the element is not a zero, then replace the element at index 'count' with this element
    for i in range(len(arr)):
        if(arr[i] != 0):
            arr[count] = arr[i]
            # increment count by 1
            count += 1

    # After all the non-zero elements have been shifted to the front of the list and 'count' is set as the index of first 0
        # make all the elements 0 from 'count' to the end of the list
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")