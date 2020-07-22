'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Create initial sub-array of size k
        # k may be too large for array
            # return error message
    # Slide sub array accross original array (nums)
        # k will vary in size,
        # so the itterations need to know when to stop
            # while loop - incremented, or
            # for loop with i stopping at len(nums) - k 
    # return max of given sub array
    # append max of sub arrays to answer array
    if k > len(nums):
        print("k value greater than size of list. Check list size.")

    list_ = []
    for i in range(0, len(nums) - k + 1):
        sub_arr = nums[i: i + k]
        list_.append(sub_arr)

    max_ = [max(array) for array in list_]
    return max_
    
    
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
