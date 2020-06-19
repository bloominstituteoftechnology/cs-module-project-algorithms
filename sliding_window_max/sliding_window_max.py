'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

#Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

def sliding_window_max(nums, k):
    # Your code here
    #loop through original (almost always original first), then loop through window array
    #need to loop through window to find max value in window

    max_values = []
    if len(nums) <= k: #if the length of nums array is less than or equal to window then we just calculate max value and add that to our empty max values array
        max_values.append(max(nums)) #max is a method in python that calculates max value
    else:
        # len(nums) >= k:
        #because the window is smaller than array its able to move left to right

        for x in range(0, len(nums)-(k-1)): #since we have window we have to have window in length thats why there is k-1
            window = max(nums[x:x + k]) #creating new window variable that will tell our contraints of our window (this window is inside the array)
            #this tells it the window to move left to right
            max_values.append(window) #window added to the max values array
    return max_values #returning max values

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
