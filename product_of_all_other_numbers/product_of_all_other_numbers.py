'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    products = [0 for _ in range(len(arr))]
    # For each int, we find the product of all the ints
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(arr)):
        products[i] = product_so_far
        product_so_far *= arr[i]
    # For each int, we find the product of all the ints
    # after it. Each index in products already has the
    # product of all the ints before it, now we're storing
    # the total product of all other ints
    product_so_far = 1
    for i in range(len(arr) - 1, -1, -1):
        products[i] *= product_so_far
        product_so_far *= arr[i]
    return products
    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
