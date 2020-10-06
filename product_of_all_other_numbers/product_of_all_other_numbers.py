'''
Input: a List of integers
Returns: a List of integers
'''
from functools import reduce

# First Pass Solution

def product_of_all_other_numbers(arr):
    # Your code here
    # product_of_numbers = 0
    # total = 0
    # make a copy of the input list
    product_list = []
    # loop over indices of input list
    for i in range(len(arr)):
        # store value of current index from input list
        total = 0
        temp = arr[i]
        # overwrite current index value with 1 to negate multiplying it
        arr[i] = 1
        # Multiply all elements in input list
        total = reduce((lambda x, y: x * y), arr)
        # restore original value for current index back to input list
        arr[i] = temp
        # append to new list
        product_list.append(total)
    # return list
    return product_list

foo = [1, 7, 3, 4]

x = product_of_all_other_numbers(foo)
print(x)
# [84, 12, 28, 21]

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
