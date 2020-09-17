'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # Initialize a result list for storing max values
    # Set a pointer for the begining and end of the sliding window being evaluated
    
    res_arr = []
    #begining sliding window(k):
    i = 0
    #end sliding window(k):
    j = k  

    #Python max() Function
    # max_val = max(nums[i:j])

    # Iterate through the original array, if the newest val (k) is greater than max_val
    #while exists index in the array - k (outside of the sliding_window(k))
    while i <= len(nums) - k:
        sliding_window = nums[i:j]
        # Set the max value for the  sliding window
        res_arr.append(max(sliding_window))
        # Increment begining and end pointers by 1 (walk foward 1 by 1 index)
        i += 1
        j += 1
    return res_arr
  


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
