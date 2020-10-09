'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    maxes = []
    end = len(nums)

    if k <= end:                            # Ensure window is not > nums length
        for i in range(0, end):             # Loop through nums
            numsSlice = nums[i:k+i]         # Create slice representing window
            maxes.append(max(numsSlice))    # Calc max and append to output array

            if k+i == end:                  # End if right side of window has reached end
                break

    return maxes

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
