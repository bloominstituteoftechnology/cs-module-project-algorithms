'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque

def sliding_window_max(nums, k):
    ''' FIRST PASS SOLUTION '''

    # # Look for the maximum value within k throughout the nums arr and store those values in a result list
    # result = []
    # index = 0
    # end_index = k

    # # If len(k) - 1 > len(nums) - 1 return because the sliding window is no longer fitting within the list
    # while index <= len(nums) - k:
    #     # Start at index 0 and create a subarray of len k (slice nums to be nums[index:k])
    #     temp_nums = nums[index:end_index]
    #     max_value = max(temp_nums)
    #     result.append(max_value)

    #     # After each pass increment indexes by 1
    #     index += 1
    #     end_index += 1

    # return result

    ''' WRITING BETTER SOLUTIONS '''

    # Setup result list to hold max values and a deque
    result = []
    dq = deque()

    # Loop through nums list
    for i, num in enumerate(nums):
        # While the element in nums at the last dq index is smaller than the current num, remove it from the deque
        while dq and nums[dq[-1]] < num:
            dq.pop()

        # If the current index minus the first deque index is greater than k, remove the first element since it's out of range for the slide    
        if dq and i - dq[0] >= k:
            dq.popleft()

        # Add index to the deque list    
        dq.append(i)

        # Append the first deque index to the results list
        result.append(nums[dq[0]])

    # Return the result list starting at k - 1
    return result[k - 1:]

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")