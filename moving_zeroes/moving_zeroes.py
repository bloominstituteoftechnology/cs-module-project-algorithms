'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # a = []
    # b = []
    # for i in arr:
    #     if i == 0:
    #         a.append(i)
    #     else: 
    #         b.append(i)
    # arr = a + b 
    # return arr

    # initialize a left and right pointer
    # left is 0
    # right is last index in arr
    left = 0
    right = len(arr)-1 
    
    while left <= right: 
        if arr[left] == 0 and arr[right] != 0:
            # swap
            arr[left], arr[right] = arr[right], arr[left]
            # increment left
            # decremnt right
            left += 1
            right -= 1
        elif arr[left] != 0:
            left += 1
        elif arr[right] == 0:
            right -= 1
    return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")