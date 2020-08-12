'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Will try an implementation that uses a queue
from collections import deque

# Trying with an array (list)

def sliding_window_max(nums, k):
    # making the maxArr that will hold all the 
    # max amounts for each window
    maxArr = []
    # making two pointers one for the right end of window
    # and another for the left end of the window
    # the end will be how far to loop in the maxArr
    # will start with 1
    # doing 2 - k to account for the first one appended  outside of the loop
    lptr = 2 - k
    #breakpoint()
    # putting the first one in ootside the loop
    maxArr.append(nums[0])
    # doing the looping through the nums array
    for i in range(1, len(nums)):
        # will be looping through those elements that are found in the 
        # window and will change the max if needed for each one of them
        
        start = 0 if 0 >= lptr else lptr
        
        for j in range(start, len(maxArr)):
                
            if maxArr[j] < nums[i]:
                maxArr[j] = nums[i]

        # will now increment the lptr and the rptr
        lptr+=1

        if i < (len(nums)-k+1):
            # making the spot for the new window
            maxArr.append(nums[i])

        
        
        
        
        
        

    return maxArr        

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
