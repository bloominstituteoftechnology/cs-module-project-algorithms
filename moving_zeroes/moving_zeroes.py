'''
Input: a List of integers
Returns: a List of integers
'''
# initialize L and R pointer 
# left is 0
# right is last index in arr

# b/c of pointers use a while loop while left <= right
    # if left points at a 0 and right points at non-zero
        # swap
        #increment left
        # decrement right
    # else 
        # if left is non-zero
            # increment left
        # if right is 0
            # decrement right
def moving_zeroes(arr):
    i = 0
    length = len(arr)

    while i < length:
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
            length -= 1
        else:
            i += 1
    
    return arr
            

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")