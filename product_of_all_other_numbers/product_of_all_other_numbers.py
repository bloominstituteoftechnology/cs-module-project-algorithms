import math
'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here

    # empty list to catch the products
    products = []

    # Create start and end points for loop
    start = 0
    end = len(arr) - 1

    # Loop through arr by using start as index
    while start <= end:
        # make a copy of arr to leave unmodified by `pop`
        c = arr.copy()
        # breakpoint()
        # print("start:", start)
        # print(c)
        # `pop` current index value
        c.pop(start)
        # now, get product of remaining copy list
        x = math.prod(c)
        # add that to products list
        products.append(x)
        # print(c)
        # breakpoint()
        # Update start
        start += 1

    return products


if __name__ == '__main__':
    # # Use the main function to test your implementation
    # # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

    # For example, given
    # ```
    # [1, 7, 3, 4]
    # ```
    # your function should return
    # ```
    # [84, 12, 28, 21]
    # ```
    # by calculating
    # ```
    # [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    # ```

    samp = [1, 7, 3, 4]
    print(product_of_all_other_numbers(samp))
    # breakpoint()
