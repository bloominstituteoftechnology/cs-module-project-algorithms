import numpy as np

'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Converts Python list to NumPy array;
    # this will allow us to use numpy.prod(np.array)
    # in our return statement
    arr = np.array(arr)
    # List for holding the arrays with given value dropped
    list_ = []
    for val in arr:
        index = np.where(arr == val)[0][0]
        # Unfortunately NumPy arrays have no pop functionality,
        # so we'll have to use list slicing here.
        if index == 0:
            drop_arr = arr[index + 1:]
        elif index == len(arr):
            drop_arr = arr[:index]
        else:
            drop_arr = list(arr[:index]) + list(arr[index + 1:])
            drop_arr = np.array(drop_arr)

        list_.append(drop_arr)

    return [np.prod(array) for array in list_]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    # arr = np.array(arr)
    # print(np.where(arr == 1)[0][0])

    print(product_of_all_other_numbers(arr))

    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
