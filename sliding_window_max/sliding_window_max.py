'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    """
    Returns an array consisting of the maximum value of each window (length of
    k) of elements.
    
        Parameters:
                nums (list): list of integers
                k (int): integer representing the size of the sliding window
                
        Returns:
                list of integers consisting of the maxinum value of each
                window.
    """
    # # empty list of big nums
    # big_nums = []

    # # loop through the list
    # for i in range(len(nums) - k + 1):
    #     # create window of k length elements 
    #     window = nums[i:(i+k)]
    #     # find the max item in that window
    #     max_num = max(window)
    #     # append it to empty list above
    #     big_nums.append(max_num)
        
    big_nums = [max(nums[i:(i+k)]) for i in range(len(nums) - k + 1)]

    return big_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
