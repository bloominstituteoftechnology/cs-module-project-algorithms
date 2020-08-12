'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # Understand:
    # Given a list with integers, move all of the zeros to the right side
    # of the list. The order of the other integers on the left side doesn't
    # matter.

    # Plan:
    # Count the zeros
    # Use a list comprehension to remove the zeros
    # append the zeros back

    # Execute:
    arr = [val for val in arr if val != 0] + [z for z in arr if z == 0]

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
