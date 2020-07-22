'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    w_min = 0
    w_max = k
    max_vals = []
    for i in nums:
        window = nums[w_min:w_max]
        max_vals.append(max(window))

        if w_max < len(nums):
            w_min += 1
            w_max += 1
        else: 
            break
    return max_vals


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
