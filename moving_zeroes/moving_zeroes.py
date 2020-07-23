'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     new_arr = []
#     for i in arr:
#         if i != 0:
#             new_arr.append(i)
#     for i in arr:
#         if i == 0:
#             new_arr.append(i)
    
#     return new_arr

# complexity O(n
# space O(1)
def moving_zeroes(arr):
    # find index of beginning and end of arr
    left = 0
    right = len(arr)-1

    # check to see that left does not cross with right index
    while left <= right:
        # if left value is 0 and right not, then swap
        if arr[left] == 0 and arr[right] !=0:
            arr[left], arr[right] = arr[right], arr[left]
            # increment/decrement our counters       
            left += 1
            right -= 1   
        else:
            # if left doesn't = 0, that's what we want.  Increment the index by 1.
            if arr[left] != 0:
                left +=1
            # if right value does = 0, that's what we want.  Decrement the index by 1.
            if arr[right] == 0:
                right -=1
    
    return arr
    




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1, -1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")