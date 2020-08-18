'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # start is with zero
    start = 0
    # end with k var
    end = k
    #max_num is empty list
    max_nums = []
    # range from 0 to the length of list add 1 - k(size of the sliding window)
    for i in range(0, len(nums)+1-k):
        sub = nums[start:end]
        max_nums.append(max(sub))
        start += 1
        end += 1


    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


