'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # loop through a copy of the array and find the zero
    for item in arr[:]:
        if item == 0:
            #we need to add the item to the end
            arr.append(item)
            # and remove it from the current location
            arr.remove(item)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")