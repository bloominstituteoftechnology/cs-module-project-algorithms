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
    # ***First Pass***
    '''
    - k is window
    - make a new array to hold temp numbers in window
    - make another array to hold expected output
    - loop (first pass is 1 so ind0, ind1, ind2 & second pass is 2 so ind1, ind2, ind3)
        - loop over numbers in window
        - append numbers to window_array
    - append window set numbers to new array
    - compare numbers in new array 
    - return max value and append it to expected output array
    '''
def sliding_window_max(nums, k):
    window_array = []
    expected_output = []
    while 0 < len(nums) - (k-1):
        for number in nums[0:k]:
            window_array.append(number)
        window_array.sort()
        max_number = window_array[k-1]
        expected_output.append(max_number)
        nums.pop(0)
        window_array = []
    return expected_output



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
