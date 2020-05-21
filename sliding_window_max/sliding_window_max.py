'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    i = 0
    max_arr = []
    while i <= len(nums) - k:
        window = nums[i:i+k]
        max_val = max(window)
        max_arr.append(max_val)
        i+=1
        
    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
