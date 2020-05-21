'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    #nieve solution not using k - refactor with dynamic window
    #new_arr = []
    # for i in range(0, len(nums) -1):
    #     if len(nums) - 1 > k:
    #         if nums[i] > nums[i + 1] and nums[i] > nums[i + 2]:
    #             new_arr.append(nums[i])
    #         elif nums[i + 1] > nums[i] and nums[i + 1] > nums[i + 2]:
    #             new_arr.append(nums[i + 1])
    #         else:
    #             new_arr.append(nums[i + 2])

    max_nums = []
    for i in range(len(nums)):
        if k <= len(nums):
            test_arr = nums[i:k]
            k += 1

            max_nums.append(max(test_arr))


    return max_nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
