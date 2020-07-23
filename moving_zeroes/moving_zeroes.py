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
    # ***First Pass***
# def moving_zeroes(arr):
#     i = 0
#     length = len(arr)

#     while i < length:
#         if arr[i] == 0:
#             arr.pop(i)
#             arr.append(0)
#             length -= 1
#         else:
#             i += 1
    
#     return arr
    #***Second Pass***
def moving_zeroes(arr):
    index = 0
    new_array = []
    number = arr[index]
    end = len(arr)
    
    while index < end:
        number = arr[index]

        if number == 0: # if number at this index is zero move it to end
            new_array.insert(end, 0) # at the end of new_array insert 0
        else:
            new_array.insert(0, number) # insert the number at the start
        index += 1
        
    return new_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")