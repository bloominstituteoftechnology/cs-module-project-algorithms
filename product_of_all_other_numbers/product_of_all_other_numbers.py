import numpy as np

'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Create empty product array,
    # loop through each value
    # create multiplication array
        # create new array, absent value
            # isolate indicies
            # slice index to remove value
        # np.prod(new_array)
    arr = np.array(arr)
    for val in arr:
        index = np.where(arr == val)[0][0]
        if index == 0:
            product_arr = arr[index + 1:]
        elif index == len(arr):
            product_arr = arr[:index]
        else:
            product_arr = list(arr[:index]) + list(arr[index + 1:])
            product_arr = np.array(product_arr)

        print(product_arr)

        


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    # arr = np.array(arr)
    # print(np.where(arr == 1)[0][0])

    product_of_all_other_numbers(arr)

    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
