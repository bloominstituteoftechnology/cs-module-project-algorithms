'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # left pointer at the beginning
    # right pointer at the end
    left, right = 0, len(arr)-1
    # loop until left and right pointers meet or right pointer passes the
    # left pointer
    while left < right:
        # swap situation:
        # left sees zero and right sees non-zero
        if arr[left] == 0 and arr[right] != 0:
            # swap the items
            arr[left], arr[right] = arr[right], arr[left]
            # increment left
            # decrement right
        # non-swap situation
            # if left sees non-zero
        if arr[left] != 0:
            # increment left
            left = left + 1
        # if right sees zero
        if arr[right] == 0:
            # decrement right
            right = right - 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")