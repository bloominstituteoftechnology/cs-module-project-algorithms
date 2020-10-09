'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_2nd(nums, k):
    # Your code here
    # start at the first element
    first_element = 0
    # the last element is always "k" away from the first element
    last_element = first_element + k
    # create a new array to store the new items
    new_array = [0] * (len(nums) - k + 1)
    
    # loop until the last element is no longer on the array
    while last_element <= len(nums):
        # get the max number from the temp array
        new_array[first_element] = max(nums[first_element:last_element])
        
        # move on to the next element
        first_element += 1
        last_element = first_element + k

    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_2nd(arr, k)}")
