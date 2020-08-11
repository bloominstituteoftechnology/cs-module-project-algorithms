'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # okay so we have current index, and we have next index, and compare. 
    # If current is zero swap.
    # if current is zero and next is zero, increment next index and verify less 
    # than the array size.

    length = len(arr)

    if length < 2:
        return arr

    i = 0
    j = 1 #starting it one past the start

    while j < length:
        if arr[i] == 0:
            if arr[j] == 0:
                j += 1
            else:
                arr[i] = arr[j]
                arr[j] = 0
        else:
            i += 1
            j += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")