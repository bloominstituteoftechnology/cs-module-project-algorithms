'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    arr = nums
    return_arr = []
    n = len(arr)
    beg = 0
    end = beg + k
    while end <= n:
        current_arr = arr[beg:end]
        return_arr.append(max(current_arr))
        beg += 1
        end += 1
    return return_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35, 68, 54, 51, 35, 36, 13, 27, 27, 24, 6, 33, 83, 97, 55, 5, 25, 85, 56, 4, 100, 38, 38, 83, 29, 1, 11, 27, 64, 99, 64, 29, 41, 95, 59, 46, 75, 67, 40, 49, 62, 30, 56, 88, 71, 77, 43, 79, 27, 65, 24, 18, 74, 50, 23, 47, 45, 60, 62, 84, 53, 2, 90, 29, 99, 75, 59, 44, 71, 7, 59, 59, 27, 72, 6, 89, 90, 40, 51, 45, 43, 86]
    k = 5

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
