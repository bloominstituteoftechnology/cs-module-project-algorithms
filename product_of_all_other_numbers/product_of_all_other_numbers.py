"""
Algorithms, problem 3
"""

def product_of_all_other_numbers(arr):
    """
    Input: a list of integers
    Returns: a list of integers
    """

    product = 1
    zeros = arr.count(0)

    if zeros <= 1:
        # One or fewer zeros mean at least one non-zero product to calculate.
        for num in arr:
            if num != 0:
                product *= num
    else:
        # Multiple zeros mean all partial products will be zero.
        for index in range(len(arr)):
            arr[index] = 0
            return arr

    for index, num in enumerate(arr):
        # Fill in partial products.
        if num != 0:
            if zeros == 1:
                arr[index] = 0
            else:
                arr[index] = product / num
        else:
            arr[index] = product

    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # test_arr = [1, 2, 3, 4, 5]
    test_arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6,
                2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7,
                7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print("Output of product_of_all_other_numbers: "
          f"{product_of_all_other_numbers(test_arr)}")
