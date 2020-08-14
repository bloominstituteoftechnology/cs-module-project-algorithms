from collections import deque

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     return [max(nums[i:k+i]) for i in range(0, len(nums) - k + 1)]

def sliding_window_max(nums, k):
    q = deque()
    q.append(0)
    for i in range(1, k):
        if nums[i] >= nums[q[0]]:
            q.clear()
            q.append(i)
        else:
            j = len(q) - 1
            while j > 0:
                if nums[i] >= nums[q[j]]:
                    q.pop()
                j -= 1
            q.append(i)

    max_val = nums[q[0]]
    max_nums = [max_val]
    for i in range(k, len(nums)):
        if i > q[0] + k - 1:
            q.popleft()
            max_val = nums[q[0]] if q else float("-inf")
        if nums[i] >= max_val:
            q.clear()
            q.append(i)
            max_val = nums[i]
        else:
            j = len(q)- 1
            while j > 0:
                if nums[i] > nums[q[j]]:
                    q.pop()
                j -= 1
            q.append(i)
        max_nums.append(nums[q[0]])
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
