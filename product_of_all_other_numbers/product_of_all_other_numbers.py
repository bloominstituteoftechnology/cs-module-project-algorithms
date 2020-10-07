'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    n = len(arr)
    if n < 1:
        return -1
    
    left_product = [0] * n
    right_product = [0] * n
    product = [0] * n

    left_product[0] = 1
    right_product[n - 1] = 1

    for i in range(1, n):
        left_product[i] = arr[i - 1] * left_product[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_product[i] = arr[i + 1] * right_product[i + 1]
    
    for i in range(n):
        product[i] = left_product[i] * right_product[i]

    return product


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1,2,3]
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
