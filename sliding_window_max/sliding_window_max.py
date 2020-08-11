'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # return [max(nums[i:k+i]) for i in range(0, len(nums) - k + 1)]
    curr_max = max(nums[0:k])
    max_arr = [curr_max]
    for i in range(1, len(nums) - k):
        print(nums[i:i+k])
        curr_max = max(curr_max, nums[i-1], nums[i+k])
        max_arr.append(curr_max)
    curr_max = max(curr_max, nums[i-1], nums[i+k])
    max_arr.append(curr_max)
    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
