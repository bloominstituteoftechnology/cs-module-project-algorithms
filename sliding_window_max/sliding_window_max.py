'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import time
def sliding_window_max(nums, k):
    # assign empty list to maxs
    maxs = []
    # for loop through nums with the end being len(nums) - k
    for i in range(0, len(nums) - (k - 1)):
        # find max from index + k and append to maxs
        current_max = max(nums[i:i+k])
        maxs.append(current_max)
    
    # return maxs
    return maxs


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
