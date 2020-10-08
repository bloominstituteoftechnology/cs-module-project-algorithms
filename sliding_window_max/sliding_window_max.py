'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    start = 0
    end = len(nums)

    max_nums = []
    for i in range(end - k + 1):
        start = nums[i]

        for num in range(1, k):

            if nums[i + num] > start:
                start = nums[i + num]

        max_nums.append(start)
        
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
