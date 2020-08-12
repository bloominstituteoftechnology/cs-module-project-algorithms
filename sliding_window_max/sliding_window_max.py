'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # First Pass:
    # Assuming K is never bigger than the array
    # start with index, then look i + 1, i + 2... i + k
    # store the greatest in the output array
    # check that i + k is never greater than the last index
    # return the output array
    # this is O(kn) time.  Since k isn't a constant, this can get ugly
    # but this is just a first pass
    output = []

    for i in range(len(nums)):
        # I did this with explicit minuses so that I didn't lose track
        # of the zero indexing. If we think of a window as primarly being
        # indices, then we have to offset k by one for zero indexing.
        if i + (k - 1) > (len(nums) - 1):
            return output

        greatest = nums[i]

        for j in range(k):
            if greatest < nums[i+j]:
                greatest = nums[i+j]
            
        output.append(greatest)


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
