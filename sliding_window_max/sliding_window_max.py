'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    temp = []
    complete = []
    start = 0
    end = k - 1
    maximum = None

    for x in range(len(nums) - end):
        for y in range(start, end + 1):
            temp.append(nums[y])
        
        mx = max(temp)
        complete.append(mx)
        temp = []
        start += 1
        end += 1
        
    return complete
            


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
