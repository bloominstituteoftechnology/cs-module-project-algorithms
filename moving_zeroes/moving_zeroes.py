'''
Input: a List of integers
Returns: a List of integers
'''
# First Pass Solution
#  
# def moving_zeroes(arr):
#     # Your code here
#     start = 0
#     end = len(arr) - 1
#     while end > start:
#         if arr[start] is 0 and arr[end] is not 0:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1
#         elif arr[start] is not 0 and arr[end] is not 0:
#             start += 1
#         else:
#             end -= 1
#     return arr

# Second Pass Solution

def moving_zeroes(arr):
    # Your code here
    # start and ending index
    start = 0
    end = len(arr) - 1
    # while start and end have not met 
    while end > start:
        # check end is 0 and start is not for swap
        if arr[start] is 0 and arr[end] is not 0:
            arr[start], arr[end] = arr[end], arr[start]
            # next for both in their directions
            start += 1
            end -= 1
        elif arr[start] is not 0 and arr[end] is not 0:
            start += 1
        # otherwise decrement end
        else:
            end -= 1
    # return input list
    return arr

arr = [1, 2, 3, 0, 4, 0, 0]
answer = moving_zeroes(arr)
print(answer)
arr = [0, 0, 0, 0, 3, 2, 1] 
answer = moving_zeroes(arr)
print(answer)

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The result of moving_zeroes is: {moving_zeroes(arr)}")

import time
zeroes = [1] * 1000000
list1 = zeroes + [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]
start_time = time.time()
moving_zeroes(list1)
end_time = time.time()
print(list1[:12])
print(f"Moving zeroes took {end_time - start_time}")
