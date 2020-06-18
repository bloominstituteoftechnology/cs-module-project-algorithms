'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here    
    a = []
    for i in range(k, len(nums) + 1):
        window = nums[i - k:i]
        # print(window, max(window))
        a.append(max(window))

    return a

    # return [max(nums[num - k: num]) for num in range(k, len(nums) + 1)]   

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
