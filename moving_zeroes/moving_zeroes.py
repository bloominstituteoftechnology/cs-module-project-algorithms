'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    index = 0
    # Take an array of integers [0, 3, 1, 0, -2] arr
    new_array = []
    # loop 
    while index < len(arr):
        number = arr[index]
        # If number == 0, capture and append
        if number == 0:
            new_array.insert(len(arr), number)
        # If number != 0, move to the left of the array
        else:
            new_array.insert(0, number)
        index += 1
    # Variable for new array to hold moved numbers
    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")