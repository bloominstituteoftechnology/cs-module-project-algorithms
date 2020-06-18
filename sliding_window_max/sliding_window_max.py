'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque 

def sliding_window_max(nums, k):
    # Your code here
    #pass
    # Too Slow But Working Solution
    # results = []
    # maximum = 0
    # for i in range(len(nums) - k + 1):
    #     maximum = nums[i]
    #     for j in range(1, k):
    #         if nums[i+j] > maximum:
    #             maximum = nums[i+j]
    #     results.append(maximum)
    # return results

    # Still too slow
    results = []
    n = len(nums)
    indices = [0 for i in range(n)]
    s = [0]

    for i in range(1, n):
        while len(s) > 0 and nums[s[-1]] < nums[i]:
            indices[s[-1]] = i - 1
            del s[-1]
        s.append(i)

    while len(s) > 0:
        indices[s[-1]] = n - 1
        del s[-1]

    j = 0
    for i in range(n - k + 1):
        while (j < i or indices[j] < i + k - 1):
            j += 1
        results.append(nums[j])
    return results











if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
