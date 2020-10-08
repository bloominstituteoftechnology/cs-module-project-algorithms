'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    max_window = []
    if len(nums) < k:
        return -1
    for index in range(0, len(nums) - k + 1):
        left_side = index
        right_side = index + k
        max_window.append(max(nums[left_side:right_side]))
    return max_window


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
