'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Code goes here

    # Old Code:
    i = 0
    arr = []
    while i + (k - 1) < len(nums):
        arr.append(max(nums[i:(i+k)]))
        i += 1

    return arr

    # the runtime of this code is O(n-(m-1)), where n is the
    # length of the array, and m is the value of k.

    # I probably cheated using the built-in python function max();
    # my code would probably be a tiny bit slower as I would
    # need to go through each value within the window and
    # determine the max value manually.

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")