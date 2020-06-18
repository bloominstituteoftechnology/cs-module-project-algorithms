'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    maxArr = [0] * (len(nums)-k+1)  #create max array, length = nums-k+1 
    for i in range(len(nums)-k+1):
        maxArr[i] = nums[i]         #set max array to nums[i] index
        for j in range(i+1, i+k):     # look for bigger number in the rest of the window
            if maxArr[i] < nums[j]:
                maxArr[i] = nums[j]
    return maxArr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
