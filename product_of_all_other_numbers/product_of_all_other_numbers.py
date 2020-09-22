
import math
'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Create a new empty array
    newArr = []
    # Loop for each item in the array
    for i in range(0, len(arr)):
        # Copy the array
        copy = arr.copy()
        # On each pass, the value at that index becomes 1, so that it won't affect the multiplication
        copy[i] = 1
        # Set the total to 1 so that we can replace it with the product of the copied array
        total = 1
        # Loop over each item in the copy array
        for val in copy:
            # Set the total to the product of each value in the copy array
            total = total * val
            # Append the total for the current iteration into the new array
        newArr.append(total)
    # Return the new array after all the loops have run
    return newArr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
