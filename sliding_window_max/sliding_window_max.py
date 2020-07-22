'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    '''
    Returns an array consisting of the max value of each window
    (length of k) of elements

    Params:
        nums (list): list of ints
        k (int): int representing sliding window size

    Returns:
        list of ints consisting of max value of each window
    '''
    # an empty list of big nums
    big_nums = []
    # loop through the list
    for i in range(len(nums) - k + 1):
        # create a window of len(k) elements
        window = nums[i:(i + k)]
        # find window's maximum
        max_num = max(window)
        # append to empty list

        return big_nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
