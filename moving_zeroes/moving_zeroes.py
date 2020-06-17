'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # We can look at this problem as if we are moving non-zeros to the left
    # But that would mean insertions at the beginning of the array
    # Or we could look at it as moving zeros to the end of the array
    # The challenge asks to do it in one pass with O(1) space

    # Iterate through numbers
    # If number is zero, move to end of array
    # If number is not zero, simply increment the index
    # We want to be looping through numbers minus number of zeros moved
    # Let's use a while loop for our iteration so that we can modify the end

    i = 0
    end = len(arr)

    while i < end:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            end -= 1
        else:
            i += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")