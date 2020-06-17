'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # initialize a resulted array
    resulted_array = []

    # for each number in the list, except the last k-1
    for i in range(len(nums)-(k-1)):
        # i is a start index for window
        # initialize an end index
        end = i + k

        # set the windows
        window = nums[i:end]
        # get the max number
        max_num = max(window)
        # add max number to the resulted array
        resulted_array.append(max_num) 

    return resulted_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
