'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Will try an implementation that uses a queue
from collections import deque

# Trying with an array (list)
# This is the first pass solution
# def sliding_window_max(nums, k):
#     # making the maxArr that will hold all the 
#     # max amounts for each window
#     maxArr = []
#     # making two pointers one for the right end of window
#     # and another for the left end of the window
#     # the end will be how far to loop in the maxArr
#     # will start with 1
#     # doing 2 - k to account for the first one appended  outside of the loop
#     lptr = 2 - k
#     #breakpoint()
#     # putting the first one in ootside the loop
#     maxArr.append(nums[0])
#     # doing the looping through the nums array
#     for i in range(1, len(nums)):
#         # will be looping through those elements that are found in the 
#         # window and will change the max if needed for each one of them
        
#         start = 0 if 0 >= lptr else lptr
        
#         for j in range(start, len(maxArr)):
                
#             if maxArr[j] < nums[i]:
#                 maxArr[j] = nums[i]

#         # will now increment the lptr and the rptr
#         lptr+=1

#         if i < (len(nums)-k+1):
#             # making the spot for the new window
#             maxArr.append(nums[i])

#     return maxArr    


# using this method to add to the deque if we want to
def add_to_dequeue_pop_if_needed(d, i, arr, lWind, rWind):
    # This is using a for loop until you find an element in the deque that is larger
    # Than the element that you are trying to put in the dequeue
    if d: # this means that the deque is not empty
        # not empty so will do the loop
        while True:
            if d:
                if arr[i] > arr[d[-1]]: # this is looking at the right end of the dequeue
                    # if in here will want to pop the right most element and then add 
                    # the current one
                    d.pop()
                else:
                    break
            else: # This is where there is no more in the dequeue
                break
    d.append(i)
    #elif not d:
        # will need to add the element of the number in the array
        #d.append(i)


    

# This is the second pass for the sliding window
def sliding_window_max(nums, k):
    maxArr = []
    # will be using a dequeue
    mDeque = deque(maxlen=k)
    # will be setting the window that is sliding
    lWindow = 0
    rWindow = -1 + k
    # doing the looping through the nums array
    for i in range(len(nums)):
        # need to check if we wnat to move the window
        if i > rWindow:
            # if in here we need to move the window
            lWindow +=1
            rWindow +=1
            # each time the window moves we need to ouput 
            # or add to the array that contains the max
            maxArr.append(nums[mDeque[0]])
            # if there are indices that are in the dequeue that are 
            # not in current window they will need to be removed
            while True:
                if mDeque[0] <= i-k:
                    mDeque.popleft()
                else:
                    break # This is hopefully to just break out of the while loop
        # we will now want to check if we want to add to the dequeue
        add_to_dequeue_pop_if_needed(mDeque, i, nums, lWindow, rWindow)
    # need to add the max in the deque
    maxArr.append(nums[mDeque[0]])
    return maxArr
    
                    

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
