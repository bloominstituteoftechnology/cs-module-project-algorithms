'''
Input: a List of integers
Returns: a List of integers
'''

### DAY 3: First Pass Solution ###
# def moving_zeroes(arr):
#     # take an array of integers [0, 3, 1, 0, -2] arr
#     # loop 
#     # if number != 0, move to the left of the array
#     # if number == 0, capture and append
#     # variable for new array to hold moved numbers
#     # return new array

#     index = 0
#     new_array = []
#     while index < len(arr):
#         number = arr[index]
#         if number == 0:
#             new_array.insert(len(arr), number)
#         else:
#             new_array.insert(0, number)
#         index += 1
#     return new_array


### DAY 4: FUNCTION OPTIMIZED ###
def moving_zeroes(arr):
    index = 0
    new_array = []
    end = len(arr)
    while index < end:
        number = arr[index]
        if number == 0: # if the number at this index is zero, we want to move it to the end
            new_array.insert(end, 0) # At the end (len(arr)) of the new_array, insert 0
        else: # otherwise
            new_array.insert(0, number) # At the beginning (new_array[0]), insert the number 
        index += 1
    return new_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


# # a one pass solution 
# def moving_zeroes(arr):
#     for i in range(len(arr)): # loop through each item of the input list
#         x = arr[i]
#         if x != 0: # if the item is non-zero
#             arr = [x] + arr[:i] + arr[i+1:] # extract from the list and place at the beginning
#     return arr

'''
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?
​
if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap
​
if the left sees a non-zero increment
if the right sees a zero increment
'''

# def moving_zeroes(arr):
#     # left pointer at the beginning
#     # right pointer at the end
# ​
#     # loop until left and right pointers meet or right pointer passes the left pointer
#         # swap situation:
#         # left sees zero and right sees non-zero
#             # swap the items
#             # increment left
#             # decrement right
#         # non-swap situation
#             # if left sees non-zero
#                 # increment left
#             # if right sees zero
#                 # decrement right
# ​
#     return arr