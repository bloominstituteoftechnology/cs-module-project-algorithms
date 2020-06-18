'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Old code
    prods = []
    for i, _ in enumerate(arr):
        nums = arr.copy()
        nums.pop(i)
        prod = 1
        for n in nums:
            prod *= n
        prods.append(prod)

    return prods

    # This completes both tests with a runtime of 0.001s
    # so I don't think I can improve it any more.
    # Also, it was written without using division from the get-go
    # so I didn't need to change anything there, either

    # I think the runtime is O(n*(n-1)), unless arr.copy()
    # is an O(n) operation, but since its runtime is already
    # so low, I don't think it matters that the Big-Oh notation
    # is exponential.

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
