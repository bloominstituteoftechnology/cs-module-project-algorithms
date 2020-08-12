'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # Understand:
    # Given an array, return a new array with the same number of indicies
    # The value in the new array should be the mathmatical product of the values
    # of every index in the original array except the matching index in the new array
    # Mutate the list in place and return it

    # Plan:
    # Loop through the list, multiplying each value as you go to get a total value
    # Loop the list again, dividing the total by the value at the current index and
    # overwiting the original value.

    total = 1
    for val in arr:
        total *= val

    for i in range(len(arr)):
        arr[i] = total / arr[i]

    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
