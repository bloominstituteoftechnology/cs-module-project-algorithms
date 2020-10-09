'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque
def sliding_window_max(nums, k):
    maxs = []
    q = deque()
    for i, n in enumerate(nums):
        # remove elements from the Queue if the current number is greater than the element
        while len(q) > 0 and n > q[-1]:
            q.pop()
        # add the num once all smaller nums have been removed from the Queue
        q.append(n)
        # calc the window range 
        window = i - k + 1
        # if the window's range == k, we'll add elements to the Queue
        if window >= 0:
            # add the max element (the first element in the Queue), to the output List 
            maxs.append(q[0])
            # check if the num on the left side of the window is going to be removed in the next iteration
            # if it is, and if that value is at the front of the Queue, we need to remove it from the Queue
            if nums[window] == q[0]:
                q.popleft()
    return maxs
    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
