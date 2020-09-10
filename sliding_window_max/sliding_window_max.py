'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Look for the maximum value within k throughout the nums arr and store those values in a result list
    # If len(k) - 1 > len(nums) - 1 return because the sliding window is no longer fitting within the list
    # Start at index 0 and create a subarray of len k (slice nums to be nums[index:k])
    # After each pass increment index by 1
    # Use recursion to go through the full nums list
    result = []
    index = 0
    end_index = k

    while index <= len(nums) - k:
        temp_nums = nums[index:end_index]
        max_value = max(temp_nums)
        result.append(max_value)
        index += 1
        end_index += 1

    return result

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")