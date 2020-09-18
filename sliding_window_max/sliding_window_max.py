'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    result = []

    max_upto = [0] * len(nums)
    s = [0]
    
    for i in range(1, len(nums)):
        while (len(s) > 0 and nums[s[-1]] < nums[i]):
            max_upto[s[-1]] = i - 1
            del s[-1]
        
        s.append(i)
    
    while (len(s) > 0):
        max_upto[s[-1]] = len(nums) - 1
        del s[-1]
    
    j = 0
    for i in range(len(nums) - k + 1):
        while (j < i or max_upto[j] < i + k - 1):
            j += 1
        result.append(nums[j])
    
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
