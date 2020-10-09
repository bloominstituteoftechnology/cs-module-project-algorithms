'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque

def sliding_window_max(nums, k):
    # win = []
    top = []
    # for i in range(len(nums) - k + 1):
    #   win = nums[i:i+k]
    #   top.append(max(win))
    # return top 
    que = deque()
    for i in range(k):
      while que and nums[i] >= nums[que[-1]]:
        que.pop()
      que.append(i)
    for i in range(k, len(nums)):
      top.append(nums[que[0]])
      while que and que[0] <= i-k:
        que.popleft()
      while que and nums[i] >= nums[que[-1]]:
        que.pop()
      que.append(i)
    top.append(nums[que[0]])
    return top





if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
