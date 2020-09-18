'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#function takes an array 
#k == length of subarray
#Loop over array, incrementing first index of k 
#compare the numbers in the window and return the largest # in that window

# def sliding_window(nums, k):
#     new_arr = []
#     n = len(arr)
#     current = 0
#     for i in range(n - k + 1):
#         current = arr[i]
#         for j in range(1, k):
            
#             new_arr.append(current)
#             current += 1
#     return new_array
"""
create a nested loop, the outer loop starting index to n-k
   Inner loop will run for len of k
   create a varibale to hold k's max value --> [] and append element
   find the max of K traversed by the inner loop
   append to the new array with a list of maximum elements with every iteration of outer loop

"""


def sliding_window_max(nums, k):
    n = len(nums)
    max = 0
    new_arr = []

    for i in range(n - k +1):
        max = nums[i]
        for j in range(1, k):
            if nums[i + j] > max:
                max = nums[i + j]
            
        new_arr.append(max)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
