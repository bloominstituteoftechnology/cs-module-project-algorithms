'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # check if the length of the array is greater than or equal to the size of the window, if not return
    max_nums = []
    if len(nums) >= k:
        # each time you loop through the array, create a new array of the elements inside the window
        for i in range(len(nums) - k + 1):
            window_nums = []
            for j in range(k):
                window_nums.append(nums[i + j])
            max_num = max(window_nums)
            # use the max function to find the max of the newly created array
            max_nums.append(max_num)
        return max_nums
    else:
        return

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
