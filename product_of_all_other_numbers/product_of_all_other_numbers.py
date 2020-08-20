'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

    index = 0
    # make a copy of the arr passed in
    copy_arr = [arr[i] for i in range(0, len(arr))]
    while index < len(arr):
        product = 1
        # loop through the copy array
        for i in range(0, len(copy_arr)):
            # skip over the index that is in line with the copied array
            if index == i:
                continue
            # multiply it
            product *= copy_arr[i]
        # set that index in the array to the product of all other indicies
        arr[index] = product
        index += 1

    return arr



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
