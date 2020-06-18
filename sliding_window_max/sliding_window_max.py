'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# Given an array of integers, there is a sliding window of size `k` 
# which is moving from the left side of the array to the right, one element at a time. 
# You can only interact with the `k` numbers in the window. 
# Return an array consisting of the maximum value of each window of elements.
#  k = 3    1  3 [-1  -3  5] 3  6  7       5 for this window set
# Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Expected Output: [3,3,5,5,6,7]

def sliding_window_max(nums, k):
    # k is window
    # make a new array to hold temp numbers in window (if k=3, hold array index0, index1, index2)
    # make another array to hold expected output
    # loop (first pass is 1, so ind0, ind1, ind2. 2nd pass is 2, so ind1, ind2, ind3)
    # append window set numbers to new array
    # compare numbers in new array (could have a big window set, consider sorting, and grab last index value)
    # return max value and append it to expected output array

    temp_numbers = []
    expected_output = []

    while 0 < len(nums):
        for i in arr:
            temp_numbers.append(i)
        return temp_numbers
        temp_numbers.sort()
        last_index = temp_numbers[-1]
        expected_output.append(last_index)
    return expected_output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
