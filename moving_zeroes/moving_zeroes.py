'''
Input: a List of integers
Returns: a List of integers
'''

# This solution takes O(1) space as requested by directions, but runs in O(n^2) time
# def moving_zeroes(arr):
#     # We can look at this problem as if we are moving non-zeros to the left
#     # But that would mean insertions at the beginning of the array
#     # Or we could look at it as moving zeros to the end of the array
#     # The challenge asks to do it in one pass with O(1) space

#     # Iterate through numbers
#     # If number is zero, move to end of array
#     # If number is not zero, simply increment the index
#     # We want to be looping through numbers minus number of zeros moved
#     # Let's use a while loop for our iteration so that we can modify the end

#     i = 0
#     end = len(arr)

#     while i < end:
#         if arr[i] == 0:
#             arr.append(arr.pop(i))
#             end -= 1
#         else:
#             i += 1

#     return arr

# # This solution takes O(n) space but runs in O(n) time
# def moving_zeroes(arr):
#     result = [0] * len(arr)

#     i = 0
#     j = len(arr) - 1

#     for num in arr:
#         if num != 0:
#             result[i] = num
#             i += 1
#         else:
#             result[j] = num
#             j -= 1
    
#     return result

# This solution takes O(1) space and runs in O(n) time
def moving_zeroes(arr):
    # Let't try just swapping positions at either end,
    # until our pointers meet in the middle

    i = 0
    j = len(arr) - 1

    while i < j:
        # Check for zero at i
        if arr[i] == 0:
            # while i is less than j
            # If j isn't zero, swap, move pointers, and break
            # Otherwise, move j down
            while i < j:
                if arr[j] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                    break
                else:
                    j -= 1
        else:
            # if not 0, increment i
            i += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


import time

zeroes = [0] * 1000000

start_time = time.time()

moving_zeroes(zeroes)

end_time = time.time()

print(f"Moving zeroes took {end_time - start_time}")