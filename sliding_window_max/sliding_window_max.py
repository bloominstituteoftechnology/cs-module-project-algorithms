'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # The simple solution would involve calculating the max 
    # for the whole window, looking at each visible value at each step of the way
    # We could optimize by storing the location of the max value found so far,
    # and comparing that to the next integer coming into view
    # What would happen when that max value goes out of view though?
    # We would then need to find the next highest value
    
    # Let's take a pass at the simple solution

    # Set up result array
    # Set up pointer for beginning and end of window
    # Move pointers until end is at end of nums
    # Loop through values in window finding largest
    # Add max to result
    # Increment start and end

    result = []
    start = 0
    end = k

    while end <= len(nums):
        max_num = nums[start]
        for i in range(start + 1, end):
            if nums[i] > max_num:
                max_num = nums[i]
        result.append(max_num)
        start += 1
        end += 1
    
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
