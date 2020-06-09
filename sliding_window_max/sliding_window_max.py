"""
Algorithms, problem 4
"""

def sliding_window_max(nums, k):
    """
    Input: a list of integers as well as an integer `k` representing the size
    of the sliding window
    Returns: a list of integers
    """
    maxima = [0] * (len(nums) - k + 1)
    for i in range(len(nums) - k + 1):
        maxima[i] = max(nums[i:i + k])

    return maxima


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3

    print("Output of sliding_window_max function is: "
          f"{sliding_window_max(arr, window_size)}")
