'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    windowStart = 0
    windowEnd = k
    
    solution = []
    window = []
    while windowEnd <= len(nums):
        maxNumber = nums[windowStart]
        for index in range(windowStart + 1, windowEnd):
            if nums[index] > maxNumber:
                maxNumber = nums[index]
        solution.append(maxNumber)
        windowStart += 1
        windowEnd += 1
    
    return solution
        

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
