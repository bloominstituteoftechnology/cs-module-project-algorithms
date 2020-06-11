import sys 
INT_MIN = -sys.maxsize -1

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    n = len(nums)
    if not n > k: 
        print("Invalid") 
        return -1
  
    max_sum = INT_MIN 
    window_sum = sum(nums[:k]) 
 
    for i in range(n-k): 
        window_sum = window_sum - nums[i] + nums[i + k] 
        max_sum = max(window_sum, max_sum) 
  
    return max_sum 


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
