'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # a = []
    # for i in range(k, len(nums) + 1):
    #     window = nums[i - k:i]
    #     print(window, max(window))
    #     a.append(max(window))
    # return a

    # expected_output = []
    # while 0 < len(nums) - (k-1):
    #     window_array = nums[0:k]
    #     expected_output.append(max(window_array))
    #     nums.pop(0)
    # return expected_output

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
