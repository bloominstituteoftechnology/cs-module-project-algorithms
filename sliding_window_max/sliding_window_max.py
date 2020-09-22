'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # created new empty list []
    new_list = []
    # loop through the array from idx 0 to len -k+1
    for idx in range(0, len(nums)-k+1):
        # create sub list [idx: idx+k]
        sub_list = nums[idx:idx+k]
        # append the max num of new array to new_list
        new_list.append(max(sub_list))
    # return new list
    return new_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
