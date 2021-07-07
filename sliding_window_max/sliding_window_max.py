'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    result = []

    for i in range(k-1, len(nums)):
        curr_max = nums[i]
        for j in range(i-k+1, i):
            if nums[j] > curr_max:
                curr_max = nums[j]
        result.append(curr_max)
    return result

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
