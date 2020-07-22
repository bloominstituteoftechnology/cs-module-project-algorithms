'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # initialize altered_array
#     altered_array = []
#     zeros = []

#     for element in arr:
#         if element != 0:
#             altered_array.append(element)
#         else:
#             zeros.append(element)
#     altered_array += zeros
#     return altered_array

# Instructor's first pass solution
# def moving_zeroes(arr): # O(n^2)
#     # loop through each item of input list
#     for i in range(len(arr)): # O(n)
#         x = arr[i]
#         # if the item is non-zero
#         if x != 0:
#             # exctract from the list and place at the beginning
#             arr = [x] + arr[:i] + arr[i+1:] # O(n)
#     return arr

"""
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?

if the left sees a zeo and the right pointer sees a non-zero
swap

if the left sees a non-zero increment
if the right sees a zero increment
"""

def moving_zeroes(arr): # O(n)
    # left pointer at the beginning
    left_pointer = 0
    # right pointer at the end
    right_pointer = len(arr)-1

    # loop until left and right pointers meet or right pointer passes the left pointer
    # right pointer is greater than left pointer
    while left_pointer < right_pointer:
        # swap situation:
        # left sees zeros and right sees non-zero
        if (arr[left_pointer]==0) and (arr[right_pointer]!=0):
            # swap
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            # increment left pointer
            left_pointer += 1
            # decremenet right pointer
            right_pointer -= 1
        # non-swap situation:
        # if both left and right see non-zero
        elif (arr[left_pointer]!=0) and (arr[right_pointer]!=0):
            # increment left
            left_pointer += 1
        # otherwise
        else:
            right_pointer -= 1   
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")