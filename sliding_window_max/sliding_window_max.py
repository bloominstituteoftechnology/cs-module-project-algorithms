"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


# def sliding_window_max(nums, k):
#     # Your code here
#     window = []
#     small = [0] * k
#     for i in range(len(nums) - k + 1):
#         small = nums[i : i + k]
#         window.append(max(small))
#     return window  c

def sliding_window_max(nums, k):
 
    maximum = [0] * (len(nums) - k + 1)

    maximum[0] = max(nums[:k])
    for i in range(1, len(nums) - k + 1):
        if nums[i - 1] == maximum[i - 1]:
            maximum[i] = max(nums[i:i + k])
        else:
            maximum[i] = max(maximum[i - 1], nums[i + k - 1])

    return maximum  # SMALL Ran 3 tests in 0.000s, LARGE Ran 1 test in 0.749s


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
