'''
Input: a List of integers as well as an integer `k` representing the size of the 
sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    maxValue = sum(nums[:k])
    p1 = 0
    p2  = k
    arr = []
    while p2 <= (len(nums)):
        print(nums[p1:p2])
        current_max = max(nums[p1:p2])
        arr.append(current_max)
        p1 += 1
        p2 += 1
    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
